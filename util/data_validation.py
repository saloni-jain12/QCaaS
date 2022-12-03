mode_list = ["verbatim", "simulation", "echo"]

def data_validate(job_string, mode):
    # check input string should be comma separated
    # Split job_strings with comma delimiter
    job_string = job_string.replace(" ", "")
    index = job_string.find(",")
    if index != -1:
        job_strings = job_string.split(",")
    else:
        # single value in job_string
        job_strings = [job_string]
    for job in job_strings:
        # Handles case if input string contains double comma
        if not job:
            return {"valid" : False,
                    "message" : "Invalid job details, should be in 'X(90), Y(180), X(90)' format"}

        # First letter should be x or y only
        if job[0].lower() != 'x' and job[0].lower() != 'y':
            return {"valid" : False,
                    "message" : "Invalid job details, should be in 'X(90), Y(180), X(90)' format"}

        # Angle should be enclosed in () small brackets only 
        if job[1] != '(' or job[-1] != ')':
            return {"valid" : False,
                    "message" : "Invalid job details, should be in 'X(90), Y(180), X(90)' format"}

        # Extract angle from brackets
        angle = job[2:-1]
        # Angle should be in range of 0-360
        if not angle.isnumeric():
            return {"valid" : False,
                    "message" : "Invalid job details, should be in 'X(90), Y(180), X(90)' format"}

        if not 0 <= int(angle) <= 360:
            return {"valid" : False,
                    "message" : "Invalid job details, angle should be in 0-360 range"}

    # Validation for mode
    if not mode.lower() in mode_list:
        return {"valid" : False,
                "message" : "Invalid mode details, Allowed modes - Verbatim, Simulation and Echo"}
 
    return {"valid" : True,
            "message" : "Valid String"}