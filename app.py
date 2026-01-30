from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

app = Flask(__name__)

# MongoDB connection
client = MongoClient(os.getenv("MONGO_URI"))
db = client["webhook_db"]
collection = db["events"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/webhook", methods=["POST"])
def github_webhook():
    data = request.json
    event_type = request.headers.get("X-GitHub-Event")

    record = {}

    # PUSH EVENT
    if event_type == "push":
        record = {
            "request_id": data["after"],
            "author": data["pusher"]["name"],
            "action": "PUSH",
            "from_branch": None,
            "to_branch": data["ref"].split("/")[-1],
            "timestamp": datetime.utcnow()
        }

    # PULL REQUEST EVENT
    elif event_type == "pull_request":
        pr = data["pull_request"]
        action = data["action"]

        record = {
            "request_id": pr["id"],
            "author": pr["user"]["login"],
            "action": "PULL_REQUEST",
            "from_branch": pr["head"]["ref"],
            "to_branch": pr["base"]["ref"],
            "timestamp": datetime.utcnow()
        }

        # MERGE EVENT (Brownie Points)
        if action == "closed" and pr["merged"]:
            record["action"] = "MERGE"

    if record:
        collection.insert_one(record)

    return jsonify({"status": "success"}), 200

@app.route("/events")
def get_events():
    events = list(collection.find({}, {"_id": 0}).sort("timestamp", -1).limit(10))
    return jsonify(events)

if __name__ == "__main__":
    app.run(debug=True)
