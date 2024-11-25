from client.client import HeyGenTranslationClient

if __name__ == "__main__":
    client = HeyGenTranslationClient(base_url="http://127.0.0.1:5000")

    # Starting a new translation job
    job_id = "translate_video_1"
    start_response = client.start_job(job_id)
    print("Start Job Response:", start_response)

    # Waiting for the job to complete
    final_status = client.pending_completion(job_id)
 
    #Final Results
    print("Final Status:", final_status)
