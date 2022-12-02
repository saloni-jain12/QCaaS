class Job:
    def __init__(self, id, value, mode, status='In-Progress', exit_code=-1, time_diff='NA'):
         self._id = id
         self._value = value
         self._mode = mode
         self._status = status
         self._exit_code = exit_code
         self._time_diff = time_diff

    # setter method for status
    def set_status(self, status):
        self._status = status

    # setter method for exit_code
    def set_exit_code(self, exit_code):
        self._exit_code = exit_code

    # setter method for time_diff
    def set_time_diff(self, time_diff):
        self._time_diff = time_diff

    # getter method
    def get_job_details(self):
        job_details = {
            "id" : self._id,
            "value" : self._value,
            "mode": self._mode,
            "status": self._status,
            "exit_code": self._exit_code,
            "time_taken": self._time_diff
        }
        return job_details

# Dictionary for jobs
jobs = {}
