import time
from typing import Iterator

import boto3

from config import Settings


class StopPolling(Exception):
    pass


class Queue:

    IDLE_TIMEOUT = 5  # seconds

    def __init__(self, queue_name: str, config: Settings):
        sqs = boto3.resource(
            "sqs",
            region_name=config.AWS_REGION,
            aws_access_key_id=config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
        )
        self._queue = sqs.get_queue_by_name(QueueName=queue_name)

    # Ref: https://github.com/aws/aws-sdk-ruby/blob/a82c8981c95a8296ffb6269c3c06a4f551d87f7d/gems/aws-sdk-sqs/lib/aws-sdk-sqs/queue_poller.rb
    def poll(self) -> Iterator[str]:
        polling_started_at = time.time()
        last_message_received_at = None

        try:
            while True:
                messages = self._queue.receive_messages()

                if len(messages) == 0:
                    since = last_message_received_at or polling_started_at
                    idle_time = time.time() - since
                    if idle_time > self.IDLE_TIMEOUT:
                        raise StopPolling

                else:
                    last_message_received_at = time.time()
                    for msg in messages:
                        yield msg.body
                        # Message deletion is neccessary, so that the queue will know that the message is processed.
                        # Without this, it'll get stuck here and therefore cannot reach the next `queue.receive_messages()`.
                        msg.delete()

        except StopPolling:
            return
