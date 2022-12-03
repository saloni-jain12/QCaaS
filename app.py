from flask import Flask, jsonify, request, make_response, abort
from flask_expects_json import expects_json
from jsonschema import ValidationError
from datetime import datetime
from model.job import *
from stub.runtime import Runtime
from util.data_validation import *
import random
import sys
import threading
import time
import uuid

app = Flask(__name__)

@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return make_response(jsonify({'error': original_error.message}), 400)
    else:
        # Validation message error for the wrong format
        return make_response(jsonify({'error': error.description}), 400)

@app.errorhandler(500)
def internal_server_error(error):
    print('Internal Server Error', error.description)
    return make_response(jsonify({'error': 'Something went wrong in server !!'}), 500)

# Schema for JSON request
schema = {
    'type': 'object',
    'properties': {
        'job': {'type': 'string'},
        'mode': {'type': 'string'}
    },
    'required': ['job', 'mode']
}

@app.route("/job", methods = ['POST'])
@expects_json(schema)
def execute_job():
    # Validate input job string and mode
    request_data = request.get_json(force=True, silent=True)

    # If request is empty: send response for invalid input format
    if not request_data:
        return jsonify({"error": "Invalid input. Please check the input format"})

    # get job and mode from input request
    job_string = request_data['job']

    job_mode = request_data['mode']
  
    validation = data_validate(job_string, job_mode)

    if not validation['valid']:
        abort(400, validation['message'])

    # Validation Success
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
            # print('*****In Runtime Thread******')
            mode = str(job.get_job_details()['mode'])
            value = str(job.get_job_details()['value'])

            if mode.lower() != 'echo':
                # instantiate Runtime object
                runtime_instance = Runtime()

                # execute runtime and calculate time difference
                start_time = datetime.now()
                job_exit_code = runtime_instance.execute(value, mode, start_time)
                end_time = datetime.now()
                tdelta = end_time - start_time
            else:
                # echo mode performed by the system
                start_time = datetime.now()
                print(f"{start_time}: Executing {value} in echo mode")
                time.sleep(3)
                job_exit_code = random.randrange(0,10)
                end_time = datetime.now()
                tdelta = end_time - start_time 

            # update job object
            status = 'Success' if job_exit_code == 0 else 'Fail'
            job.set_time_diff(str(tdelta.total_seconds()) + ' secs')
            job.set_exit_code(job_exit_code)
            job.set_status(status)
        except:
            print("Something went wrong in the system", sys.exc_info()[0])

    thread = threading.Thread(target=execute_runtime, kwargs={'job': job})
    thread.start()

    return jsonify({"jobID" : job_id})


@app.route('/job', methods=['GET'])
def return_job():
    id = request.args.get('id')
    job_id = jobs.get(id)
    if not job_id:
        return jsonify({"error": "Invalid Job Id"})
    else:
        return job_id.get_job_details()

if __name__ == "__main__":
    app.run(debug=True)