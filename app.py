from flask import Flask, jsonify, request, make_response
from flask_expects_json import expects_json
from jsonschema import ValidationError
from  util.data_validation import *
from model.job import *
import uuid
import threading
from stub.runtime import Runtime
from datetime import datetime
import time, random
import sys


app = Flask(__name__)

@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return make_response(jsonify({'error': original_error.message}), 400)
    return error

schema = {
    'type': 'object',
    'properties': {
        'job': {'type': 'string'},
        'mode': {'type': 'string'}
    },
    'required': ['job', 'mode']
}

# jobs = {}

@app.route("/job", methods = ['POST'])
@expects_json(schema)
def execute_job():
    ####### Validation ######
    # 1) Validate input job string and mode
    request_data = request.get_json(force=True, silent=True)

    # If request is empty: send response for invalid input format
    if (not request_data):
        return jsonify({"error": "Invalid input. Please check the input format"})

    # get job and mode from input request
    job_string = request_data['job']

    job_mode = request_data['mode']


    # if (not data_validate(job_string, job_mode)):
    #     return jsonify({"error" : "Invalid input data"})
    
    validation = data_validate(job_string, job_mode)

    if not validation['valid']:
        return jsonify({"error": validation['message']}, 400)

    ##### Validation Success #####
    # 1) Generate UUID and create job instance
    # 2) Return response to Client
    # 3) Execute runtime in separate thread asynchronously
    # 4) update job status

    # Create unique job id
    job_id = str((uuid.uuid1()).int)

    # Instantiate Job object
    job = Job(job_id, job_string, job_mode)

    # Append the object in jobs dict
    jobs[job_id] = job

    def execute_runtime(job):
        try:
            print('*****In thread******')
            print(job.get_job_details())
            mode = str(job.get_job_details()['mode'])
            value = str(job.get_job_details()['value'])

            if (mode.lower() != 'echo'):
                # instantiate Runtime object
                runtime_instance = Runtime()

                # ececute runtime and calculate time difference
                start_time = datetime.now()
                job_exit_code = runtime_instance.execute(value, mode)
                end_time = datetime.now()
                tdelta = end_time - start_time

                # update job object
                # job.set_time_diff(tdelta.total_seconds() + ' secs')
                # job.set_exit_code(job_exit_code)
                # job.set_status('complete')
            else:
                # echo mode performed by the system
                start_time = datetime.now()
                print(f"Executing {value} in echo mode")
                time.sleep(3)
                job_exit_code = random.randrange(0,10)
                end_time = datetime.now()
                tdelta = end_time - start_time 

            # update job object
            # exit_code = 0 if job_exit_code == 0 else -1
            status = 'Success' if job_exit_code == 0 else 'Fail'
            job.set_time_diff(str(tdelta.total_seconds()) + ' secs')
            job.set_exit_code(job_exit_code)
            job.set_status(status)
        except:
            print("Something went wrong in the system", sys.exc_info()[0])

    thread = threading.Thread(target=execute_runtime, kwargs={'job': job})
    thread.start()

    return jsonify({"jobID" : job_id})


@app.route('/job/<string:job_id>', methods=['GET'])
def returnJob(job_id):
    job = jobs.get(job_id)
    if not job:
        return jsonify({"error": "Invalid Job Id"})
    else:
        return job.get_job_details()


if __name__ == "__main__":
    app.run(debug=True)