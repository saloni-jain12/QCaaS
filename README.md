# QCaaS - Technical Test

## Setup

This application is build and tested on 64 bit Windows 11 with 4GB RAM.

Create and activate the virtual environment on Windows

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

## Requirements

Python >= 3.6

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)