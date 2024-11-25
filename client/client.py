import requests
import time

class HeyGenTranslationClient:

    def __init__(self,base_url,polling = 3):
        """
        This function is used to initialize the client.
        :param base_url: This is the Base URL of the client. Ex (http://127.0.0.1.5000)
        :param polling: The time in seconds for polling between sessions
        """
        self.base_url = base_url
        self.polling = polling

    def start_job(self,job_id):
        """
        This function is used to start the video translation
        :param job_id: Unique identifier for the job
        :return: Response from the server as a dictionary.
        """

        try:
            response = requests.post(f"{self.base_url}/start",json={"job_id": job_id})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error":str(e)}
    
    def get_status(self,job_id):
        """
        This function checks the status of the given job id
        :param job_id: Unique identifier for the job
        :return: Status of the job as a dictionary.
        """

        try:
            response = requests.get(f"{self.base_url}/status", params={"job_id": job_id})
            
            response.raise_for_status()
            return response.json()
        
        except requests.RequestException as e:
            return {"error":str(e)}
        
    def pending_completion(self,job_id):
        """
        Wait for a job to complete with periodic polling.
        :param job_id: Unique identifier for the job.
        :return: Final status of the job as a dictionary.
        """
        while True:
            status = self.get_status(job_id)

            if "status" in status and status["status"] in ["completed", "error"]:
                return status
            
            if "error" in status:
                return status  # Stop waiting if there's an error
            
            #Polling and pending
            print(f"Job {job_id} is still pending...")  
            time.sleep(self.polling)
