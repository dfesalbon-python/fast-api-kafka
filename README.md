# Python Kafka

## Pre-requisite

- Installed Docker on your computer
- Python installed with necessary packages (python kafka, fast-api, etc.)
- Git installed on your computer
- Postman installed on your computer
- Knowledge in REST APIs and HTTP requests

## Instructions
Clone the repository `https://github.com/python-realm/fast-api-kafka.git`:
```sh
git clone https://github.com/python-realm/fast-api-kafka.git
```
Open a terminal inside the repository folder and execute 'docker compose up' to pull the zookeeper and kafka images and run the container:
```sh
docker compose up
```
Before proceeding to the next step make sure the containers are running.

Open new terminal inside the repository folder and run:
```sh
python main.py
```
This will run the main FAST API service on localhost:8000.

Open new terminal inside the repository folder and run:
```sh
python receive.py
```
Check both of the terminals. On terminal where `main.py` is executed, you will see some logs like this:
```sh
INFO:     Started server process [8524]
INFO:     Waiting for application startup.
INFO:     Application startup complete.   
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```
On terminal where `received.py` is executed, you will see some logs like this:
```sh
started listening..
```
Open a postman and send a POST request on `http://127.0.0.1:8000` with request body:
```sh
{
    "id":"123",
    "first_name": "Juan",
    "last_name": "Dela Cruz"
}
```
Check the request response and the logs on the terminal where receive.py is executed. 

You now have a working FAST API kafka messaging service. :)