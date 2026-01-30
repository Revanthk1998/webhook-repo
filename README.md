# GitHub Webhook Activity Tracker

This project implements a complete GitHub webhook workflow that captures repository
activities and displays them in a clean, minimal UI.

The system listens to GitHub webhook events such as Push, Pull Request, and Merge,
stores the required data in MongoDB, and displays the latest activity by polling
the database every 15 seconds.

This implementation follows the exact requirements of the Developer Assessment Task.

---

## Repositories Used

1. **action-repo**  
   Used to trigger GitHub events such as push, pull request, and merge.

2. **webhook-repo**  
   Flask-based backend that receives webhook events, stores data in MongoDB,
   and serves a UI to display repository activity.

---

## Technology Stack

- Python (Flask)
- MongoDB
- GitHub Webhooks
- HTML and JavaScript
- ngrok (for local webhook testing)

---

## Application Flow

1. A GitHub action (push, pull request, or merge) occurs in `action-repo`
2. GitHub sends a webhook payload to the Flask `/webhook` endpoint
3. Flask extracts only the required information from the payload
4. Event data is stored in MongoDB
5. The UI polls the backend every 15 seconds
6. Latest repository activity is displayed on the UI

---

## MongoDB Data Structure

Each webhook event is stored with the following fields:

- `author`
- `action` (PUSH / PULL_REQUEST / MERGE)
- `from_branch`
- `to_branch`
- `timestamp`

---

## UI Output Formats

### Push Event
```
{author} pushed to {to_branch} on {timestamp}
```

### Pull Request Event
```
{author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}
```

### Merge Event
```
{author} merged branch {from_branch} to {to_branch} on {timestamp}
```

---

## How to Run Locally

1. Clone the webhook repository
```bash
git clone <webhook-repo-url>
cd webhook-repo
```

2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables  
Create a `.env` file with the following:
```
MONGO_URI=<your_mongodb_connection_string>
```

5. Run the Flask application
```bash
python app.py
```

The application runs at:
```
http://localhost:5000
```

---

## Webhook Configuration

- Webhooks are configured in `action-repo`
- Payloads are sent to the `/webhook` endpoint
- Enabled events:
  - Push
  - Pull requests
- ngrok is used to expose the local Flask server during development

---

## Status

- GitHub webhook integration completed
- MongoDB persistence implemented
- UI polling every 15 seconds implemented
- Push, Pull Request, and Merge events handled
- End-to-end testing verified using ngrok

---

## Notes

- ngrok URLs are temporary and used only for local testing
- Environment files (`.env`) and virtual environments (`venv`) are not committed
- Reviewers are expected to evaluate the code and architecture

---

## Conclusion

This project fulfills all requirements of the Developer Assessment Task by
demonstrating webhook handling, backend processing, database storage, and
frontend polling in a clean and minimal implementation.
