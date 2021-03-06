# std lib
from datetime import datetime
import json
import os
import time
import uuid

# third party imports
from pykafka import KafkaClient
from pykafka.utils.compat import Empty

KAFKA_ADDR = os.getenv("KAFKA_ADDR")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")


client = KafkaClient(hosts=KAFKA_ADDR)
topic = client.topics[KAFKA_TOPIC]


def read_file(file):
    path = os.path.dirname(os.path.realpath(__file__))

    data = []
    with open(f"{path}/{file}") as json_file:
        data = json.load(json_file)

    return data


with topic.get_producer(
    min_queued_messages=1, max_queued_messages=1, delivery_reports=True
) as producer:

    events = read_file("events.json")

    partition_key = str.encode(str(uuid.uuid4()))
    for event in events:
        parition_key = str(event["id"]).encode()
        payload = json.dumps(event).encode()

        producer.produce(payload, partition_key=parition_key)

        msg, exc = producer.get_delivery_report(block=True)
        if exc is not None:
            print("Failed to deliver msg {}: {}".format(msg.partition_key, repr(exc)))
        else:
            print("Successfully delivered msg {}".format(msg.partition_key))

    print("waiting for all messages to be written")
    producer._wait_all()
