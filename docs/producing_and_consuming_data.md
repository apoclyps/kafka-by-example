Producing and Consuming Data
============================

To generate data and view it has been created successfully you can run the producer and consumer via the following commands:

```sh
docker-compose run consumer
docker-compose run producer
```

#### Example of a simple producer

```python
# std lib
from datetime import datetime
import uuid
import time
import os

# third party imports
from pykafka import KafkaClient
from pykafka.utils.compat import Empty

KAFKA_ADDR = os.getenv("KAFKA_ADDR")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")


client = KafkaClient(hosts=KAFKA_ADDR)
topic = client.topics[KAFKA_TOPIC]


with topic.get_producer(
    min_queued_messages=1, max_queued_messages=1, delivery_reports=True
) as producer:
    partition_key = str.encode(str(uuid.uuid4()))
    for i in range(10):
        test_message = f"test message {str(i)} {datetime.now()}"
        producer.produce(str.encode(test_message), partition_key=partition_key)

        msg, exc = producer.get_delivery_report(block=True)
        if exc is not None:
            print("Failed to deliver msg {}: {}".format(msg.partition_key, repr(exc)))
        else:
            print("Successfully delivered msg {}".format(msg.partition_key))

    print("waiting for all messages to be written")
    producer._wait_all()
```

### Example of a simple consumer

```python
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
```
