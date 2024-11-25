
# Video Translation Simulation

This project simulates a backend video translation service and provides a client library to interact with it. The server mimics a video translation process by managing job statuses (e.g., "pending", "completed", "error") and introduces a configurable delay to simulate processing.

---

## Usage

### 1. Start the Server
Run the server to handle job requests:
```bash
python server/server.py
```
The server will run on `http://127.0.0.1:5000`.

---

### 2. Use the Client Library
Here’s an example of how to interact with the server using the client library:

```python
from client.client import HeyGenTranslationClient

# Initialize the client
client = HeyGenTranslationClient(base_url="http://127.0.0.1:5000")

# Start a new job
response = client.start_job("translate_video_1")
print("Job Start Response:", response)

# Wait for the job to complete
status = client.pending_completion("translate_video_1")
print("Final Status:", status)
```

Run your script:
```bash
python integration_test.py
```

---

## API Reference

### Server Endpoints

#### `POST /start`
Start a new translation job.

- **Request Body**:
  ```json
  {
    "job_id": "<unique-job-id>"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Job started",
    "job_id": "<unique-job-id>"
  }
  ```

---

#### `GET /status`
Check the current status of a job.

- **Query Parameters**:
  - `job_id` (string): The unique ID of the job.

- **Response**:
  ```json
  {
    "job_id": "<unique-job-id>",
    "status": "pending | completed | error"
  }
  ```

---

## Configuration

You can adjust the delay for job processing by modifying `MIMIC_JOB_PROCESSING_TIME` in `server/server.py`.

---

## Testing

You can test the integration by running:
```bash
python test_client.py
```

This script starts a job, polls the server for its status, and prints the final result.

---

## Example Output

```bash
Job Start Response: {'message': 'Job successfully recieved', 'job_id': 'translate_video_1'}
Job translate_video_1 is still pending...
Job translate_video_1 is still pending...
Final Status: {'job_id': 'translate_video_1', 'status': 'completed'}
```

