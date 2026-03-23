import json
import os

from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
TOPIC_ID = "todo-submit-topic"
PROJECT_ID = os.getenv("GCP_PROJECT_ID") or ""

topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)


def publish_todos(todos):
  data = json.dumps(todos).encode("utf-8")
  publisher.publish(topic_path, data=data)
