Kafka REST
==========

The Kafka REST Proxy provides a RESTful interface to a Kafka cluster. It makes it easy to produce and consume messages, view the state of the cluster, and perform administrative actions without using the native Kafka protocol or clients. Examples of use cases include reporting data to Kafka from any frontend app built in any language, ingesting messages into a stream processing framework that doesn't yet support Kafka, and scripting administrative actions. ## Quickstart The following assumes you have Kafka, the schema registry, and an instance of the REST Proxy running using the default settings and some topics already created.

#### Get a list of topics

```sh
$ curl "http://localhost:8083/topics"
```

```json
[  
   {  
      "name":"events-v0",
      "num_partitions":1
   }
]
```

#### Produce a message using binary embedded data with value "Kafka" to the topic events-v0

The following payload has been base64 encoded for transmission over the wire using https://www.base64encode.org/.

```json
{
  "category": "Open Industry Index Social",
  "created": "2018-07-29T13:52:43.892339",
  "deleted": null,
  "description": "<p>A general space for anybody interested in open technologies (open source, open data or otherwise), to catch up and relax after work on Friday fortnights. People of all backgrounds, interests, skillsets and disciplines welcome.</p> <p>The Open Industry concept itself is about the ability of microentities and small businesses to collaborate formally on projects large and small, facilitated by open technologies - so we are combining the twin aims of:</p> <p>- giving tech freelancers, contractors and indies of all walks of technology life a focal point for an end-of-week (we need one too...), and</p> <p>- helping independents (and those considering a future step out) to link up to get sustainable open projects off the ground.</p>",
  "duration": 10000,
  "end": "2018-08-31T17:45:00",
  "entry": [
    {
      "description": null,
      "id": "f2a30c3b-aec6-46d7-ab34-b6f5b27c7955",
      "type": "free"
    }
  ],
  "id": "613119d5-f9ea-47d9-a9a9-42a39abdd036",
  "meetup": [

  ],
  "name": "Fortnightly Social",
  "source": "meetup",
  "start": "2018-08-31T17:45:00",
  "topics": [
    "open source", "linux"
  ],
  "updated": "2018-07-29T13:52:43.892346",
  "url": "https://www.meetup.com/Open-Industry-Index-Social/events/xcbqjpyxlbpc/"
}
```

> Note: The base64 value must be encoded using valid formatting and linted.

```sh
$ curl -X POST -H "Content-Type: application/vnd.kafka.binary.v1+json" --data '{"records":[{"value":"ewoJImNhdGVnb3J5IjogIk9wZW4gSW5kdXN0cnkgSW5kZXggU29jaWFsIiwKCSJjcmVhdGVkIjogIjIwMTgtMDctMjlUMTM6NTI6NDMuODkyMzM5IiwKCSJkZWxldGVkIjogbnVsbCwKCSJkZXNjcmlwdGlvbiI6ICI8cD5BIGdlbmVyYWwgc3BhY2UgZm9yIGFueWJvZHkgaW50ZXJlc3RlZCBpbiBvcGVuIHRlY2hub2xvZ2llcyAob3BlbiBzb3VyY2UsIG9wZW4gZGF0YSBvciBvdGhlcndpc2UpLCB0byBjYXRjaCB1cCBhbmQgcmVsYXggYWZ0ZXIgd29yayBvbiBGcmlkYXkgZm9ydG5pZ2h0cy4gUGVvcGxlIG9mIGFsbCBiYWNrZ3JvdW5kcywgaW50ZXJlc3RzLCBza2lsbHNldHMgYW5kIGRpc2NpcGxpbmVzIHdlbGNvbWUuPC9wPiA8cD5UaGUgT3BlbiBJbmR1c3RyeSBjb25jZXB0IGl0c2VsZiBpcyBhYm91dCB0aGUgYWJpbGl0eSBvZiBtaWNyb2VudGl0aWVzIGFuZCBzbWFsbCBidXNpbmVzc2VzIHRvIGNvbGxhYm9yYXRlIGZvcm1hbGx5IG9uIHByb2plY3RzIGxhcmdlIGFuZCBzbWFsbCwgZmFjaWxpdGF0ZWQgYnkgb3BlbiB0ZWNobm9sb2dpZXMgLSBzbyB3ZSBhcmUgY29tYmluaW5nIHRoZSB0d2luIGFpbXMgb2Y6PC9wPiA8cD4tIGdpdmluZyB0ZWNoIGZyZWVsYW5jZXJzLCBjb250cmFjdG9ycyBhbmQgaW5kaWVzIG9mIGFsbCB3YWxrcyBvZiB0ZWNobm9sb2d5IGxpZmUgYSBmb2NhbCBwb2ludCBmb3IgYW4gZW5kLW9mLXdlZWsgKHdlIG5lZWQgb25lIHRvby4uLiksIGFuZDwvcD4gPHA+LSBoZWxwaW5nIGluZGVwZW5kZW50cyAoYW5kIHRob3NlIGNvbnNpZGVyaW5nIGEgZnV0dXJlIHN0ZXAgb3V0KSB0byBsaW5rIHVwIHRvIGdldCBzdXN0YWluYWJsZSBvcGVuIHByb2plY3RzIG9mZiB0aGUgZ3JvdW5kLjwvcD4iLAoJImR1cmF0aW9uIjogMTAwMDAsCgkiZW5kIjogIjIwMTgtMDgtMzFUMTc6NDU6MDAiLAoJImVudHJ5IjogW3sKCQkiZGVzY3JpcHRpb24iOiBudWxsLAoJCSJpZCI6ICJmMmEzMGMzYi1hZWM2LTQ2ZDctYWIzNC1iNmY1YjI3Yzc5NTUiLAoJCSJ0eXBlIjogImZyZWUiCgl9XSwKCSJpZCI6ICI2MTMxMTlkNS1mOWVhLTQ3ZDktYTlhOS00MmEzOWFiZGQwMzYiLAoJIm1lZXR1cCI6IFtdLAoJIm5hbWUiOiAiRm9ydG5pZ2h0bHkgU29jaWFsIiwKCSJzb3VyY2UiOiAibWVldHVwIiwKCSJzdGFydCI6ICIyMDE4LTA4LTMxVDE3OjQ1OjAwIiwKCSJ0b3BpY3MiOiBbIm9wZW4gc291cmNlIiwgImxpbnV4Il0sCgkidXBkYXRlZCI6ICIyMDE4LTA3LTI5VDEzOjUyOjQzLjg5MjM0NiIsCgkidXJsIjogImh0dHBzOi8vd3d3Lm1lZXR1cC5jb20vT3Blbi1JbmR1c3RyeS1JbmRleC1Tb2NpYWwvZXZlbnRzL3hjYnFqcHl4bGJwYy8iCn0="}]}' "http://localhost:8083/topics/events-v0"
```

```json
{  
   "offsets":[  
      {  
         "partition":1,
         "offset":1
      }
   ]
}
```

#### Create a consumer for binary data, starting at the beginning of the topic's log.

```sh
$ curl -X POST -H "Content-Type: application/vnd.kafka.v1+json" \
      --data '{"format": "binary", "auto.offset.reset": "smallest"}' \
      http://localhost:8083/consumers/my_binary_consumer
```

```json
{  
   "instance_id":"rest-consumer-9ebca6d0-f967-4806-a820-fc6f8857d483",
   "base_uri":"http://localhost:8083/consumers/my_binary_consumer/instances/rest-consumer-9ebca6d0-f967-4806-a820-fc6f8857d483"
}
```

Then consume some data from a topic using the base URL in the first response. You will need to update the rest-consumer-uuid to match the consumer returned from the server. e.g. `rest-consumer-9ebca6d0-f967-4806-a820-fc6f8857d483`

```sh
$ curl -X GET -H "Accept: application/vnd.kafka.binary.v1+json" \
      http://localhost:8083/consumers/my_binary_consumer/instances/rest-consumer-9ebca6d0-f967-4806-a820-fc6f8857d483/topics/events-v0
```

```json
[  
   {  
      "key":null,
      "value":"S2Fma2E=",
      "partition":0,
      "offset":0
   }
]
```

Finally, close the consumer with a DELETE to make it leave the group and clean up its resources.

```sh
$ curl -X DELETE \
      http://localhost:8083/consumers/my_binary_consumer/instances/rest-consumer-9ebca6d0-f967-4806-a820-fc6f8857d483
```

No content in response

#### Finally, clean up.

```sh
$ curl -X DELETE \
      http://localhost:8083/consumers/my_binary_consumer/instances/rest-consumer-9ebca6d0-f967-4806-a820-fc6f8857d483
```

No content in response
