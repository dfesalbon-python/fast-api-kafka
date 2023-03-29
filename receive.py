import json
from fastapi import FastAPI
from kafka import KafkaConsumer, KafkaProducer

EMP_TOPIC = "emp_details"

app = FastAPI()
consumer = KafkaConsumer(EMP_TOPIC, bootstrap_servers="localhost:29092")
producer = KafkaProducer(bootstrap_servers="localhost:29092")


print("started listening..")
while True:
    for message in consumer:
        print("receiving data..")

        consumed_message = json.loads(message.value.decode())

        id = consumed_message["id"]
        first_name = consumed_message["first_name"]
        last_name = consumed_message["last_name"]

        data = {
            "id": id,
            "first_name": first_name,
            "last_name": last_name
        }

        print("data: " + str(data))
        print(" ")
