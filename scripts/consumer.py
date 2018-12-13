# std lib
import os

# third party imports
from pykafka import KafkaClient

KAFKA_ADDR = os.getenv("KAFKA_ADDR")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")


client = KafkaClient(hosts=KAFKA_ADDR)

topic = client.topics[KAFKA_TOPIC]
consumer = topic.get_simple_consumer()
for message in consumer:
    if message is not None:
        print(message.offset, message.value)
