import json

job_ids =[]

def test_Echo_request(app, client):
    data = {
    "job": "Y(89), X(90)",
    "mode": "Echo"
    }
    res = client.post('/job', json=data)
    assert res.status_code == 200
    res_data = int(res.json["jobID"])
    job_ids.append(res_data)
    assert res_data > 0

def test_echo_request(app, client):
    data = {
    "job": "Y(89), X(90)",
    "mode": "echo"
    }
    res = client.post('/job', json=data)
    assert res.status_code == 200
    res_data = int(res.json["jobID"])
    job_ids.append(res_data)
    assert res_data > 0

def test_simulation_request(app, client):
    data = {
    "job": "Y(89), X(90)",
    "mode": "simulation"
    }
    res = client.post('/job', json=data)
    assert res.status_code == 200
    res_data = int(res.json["jobID"])
    job_ids.append(res_data)
    assert res_data > 0

def test_Simulation_request(app, client):
    data = {
    "job": "Y(89), X(90)",
    "mode": "Simulation"
    }
    res = client.post('/job', json=data)
    assert res.status_code == 200
    res_data = int(res.json["jobID"])
    job_ids.append(res_data)
    assert res_data > 0

def test_verbatim_request(app, client):
    data = {
    "job": "Y(89), X(90)",
    "mode": "verbatim"
    }
    res = client.post('/job', json=data)
    assert res.status_code == 200
    res_data = int(res.json["jobID"])
    job_ids.append(res_data)
    assert res_data > 0

def test_Verbatim_request(app, client):
    data = {
    "job": "Y(89), X(90)",
    "mode": "Verbatim"
    }
    res = client.post('/job', json=data)
    assert res.status_code == 200
    res_data = int(res.json["jobID"])
    job_ids.append(res_data)
    assert res_data > 0

def test_invallid_request_semicolon(app, client):
    data = {
    "job": "Y(89); X(90)",
    "mode": "Verbatim"
    }
    res = client.post('/job', json=data)
    assert res.status_code == 400
    res_data = res.json["error"]
    assert res_data == "Invalid job details, should be in 'X(90), Y(180), X(90)' format"

def test_invallid_request_doublecomma(app, client):
    data = {
    "job": "Y(89),, X(90)",
    "mode": "Verbatim"
    }
    res = client.post('/job', json=data)
    assert res.status_code == 400
    res_data = res.json["error"]
    assert res_data == "Invalid job details, should be in 'X(90), Y(180), X(90)' format"

def test_invallid_request_otherThanXY(app, client):
    data = {
    "job": "Y(89), R(90)",
    "mode": "Verbatim"
    }
    res = client.post('/job', json=data)
    assert res.status_code == 400
    res_data = res.json["error"]
    assert res_data == "Invalid job details, should be in 'X(90), Y(180), X(90)' format"

def test_invallid_request_missingBracket(app, client):
    data = {
    "job": "Y(89), X90)",
    "mode": "Verbatim"
    }
    res = client.post('/job', json=data)
    assert res.status_code == 400
    res_data = res.json["error"]
    assert res_data == "Invalid job details, should be in 'X(90), Y(180), X(90)' format"

def test_invallid_request_specialChar(app, client):
    data = {
    "job": "Y(89)@ X(90)",
    "mode": "Verbatim"
    }
    res = client.post('/job', json=data)
    assert res.status_code == 400
    res_data = res.json["error"]
    assert res_data == "Invalid job details, should be in 'X(90), Y(180), X(90)' format"

def test_invallid_request_invalidAngle(app, client):
    data = {
    "job": "Y(89), X(590)",
    "mode": "Verbatim"
    }
    res = client.post('/job', json=data)
    assert res.status_code == 400
    res_data = res.json["error"]
    assert res_data == "Invalid job details, angle should be in 0-360 range"

def test_invallid_request_missingJob(app, client):
    data = {
    "mode": "Verbatim"
    }
    res = client.post('/job', json=data)
    assert res.status_code == 400
    res_data = res.json["error"]
    assert res_data == "'job' is a required property"

def test_invallid_request_missingMode(app, client):
    data = {
    "job": "Y(89), X(590)"
    }
    res = client.post('/job', json=data)
    assert res.status_code == 400
    res_data = res.json["error"]
    assert res_data == "'mode' is a required property"

def test_invallid_request_invalidMode(app, client):
    data = {
    "job": "Y(89), X(90)",
    "mode": "abc"
    }
    res = client.post('/job', json=data)
    assert res.status_code == 400
    res_data = res.json["error"]
    assert res_data == "Invalid mode details, Allowed modes - Verbatim, Simulation and Echo"

def test_get_job(app, client):
    param = str(job_ids[0])
    res = client.get(f'/job?id={param}')
    assert res.status_code == 200
    res_data = int(res.json['id'])
    assert res_data == job_ids[0]

