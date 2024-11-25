from flask import Flask,request,jsonify
import time
import threading


app = Flask(__name__)
jobs = {}
MIMIC_JOB_PROCESSING_TIME = 6

def simulate_processing(job_id):
    """
    Function that simulates job processing time
    :param job_id: Unique identifier for job
    """
    time.sleep(MIMIC_JOB_PROCESSING_TIME)
    if job_id in jobs:
        #Job Status
        jobs[job_id] = 'completed'

@app.route('/start',methods=['POST'])
def start_job():
    """
    Start a new translation job.
    - Expects a JSON with a `job_id`.
    - Initializes the job with status 'pending' and starts processing.
    """

    job_id = request.json.get('job_id')

    if not job_id:
        return jsonify({'error':'Job was not recieved'}),400
    
    if job_id in jobs:
        return jsonify({'error':'Job Id is already in current Jobs'}),404
    
    #Job Status
    jobs[job_id] = 'pending'

    threading.Thread(target=simulate_processing, args=(job_id,)).start()

    return jsonify({'message':'Job successfully recieved','job_id':job_id})


@app.route('/status',methods=['GET'])
def get_status():
    """
    Get the status of a job.
    - Expects a query parameter `job_id`.
    - Returns the status of the job.
    """

    job_id = request.args.get('job_id')

    if not job_id:
        return jsonify({'error':'Job Id was not received'}),400
    
    if job_id not in jobs:
        return jsonify({'error':'Job Id was not found in current Jobs'}),404
    
    return jsonify({'job_id': job_id,'status': jobs[job_id]})

if __name__ == '__main__':
    app.run(debug=True)