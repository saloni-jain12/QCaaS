# QCaaS - Technical Test

## Setup

This application is build and tested on 64 bit Windows 11 with 4GB RAM.

Create and activate the virtual environment on Windows PowerShell

```bash
python -m venv venv
./venv/Scripts/activate
```

Install the dependencies in virtual environment
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run the server

```bash
python app.py
```

Run the tests

```bash
python -m pytest
```

The server will be up on [http://localhost:5000](http://localhost:5000).

## API Endpoints

Client sends POST request with job and mode to application and receives Job ID in response

```bash
curl -i -X POST -H "Content-Type:application/json" -d "{\"job\": \"Y(89), X(90)\",\"mode\": \"echo\"}" http://localhost:5000/job
```

Expected Output: Applications sends back Job ID in response

```bash
{
    "jobID": "105528800897761760691894769894988597352"
}
```


Client sends GET request with Job ID to get details about the job

```bash
curl --location --request GET "http://localhost:5000/job?id=105528800897761760691894769894988597352" 
```

Expected Output: Returns details about the Job from the application

```bash
{
    "exit_code": 0,
    "id": "105528800897761760691894769894988597352",
    "mode": "echo",
    "status": "Success",
    "time_taken": "3.004326 secs",
    "value": "Y(89), X(90)"
}
```

## Requirements

Python >= 3.6

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)