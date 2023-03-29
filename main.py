import uvicorn
import json
from fastapi import FastAPI
from models import Employee
from kafka import KafkaProducer, KafkaConsumer

app = FastAPI()

EMP_TOPIC = "emp_details"

producer = KafkaProducer(bootstrap_servers="localhost:29092")


@app.post('/')
def post_data(employee: Employee):

    data = {
        "id": employee.id,
        "first_name": employee.first_name,
        "last_name": employee.last_name
    }

    producer.send(EMP_TOPIC, json.dumps(data).encode("utf-8"))
    res = {"response": "data has been sent!"}
    return res


if __name__ == "__main__":
    uvicorn.run('main:app', port=8000, reload=False)
