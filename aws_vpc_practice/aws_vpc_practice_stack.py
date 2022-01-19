from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_s3 as s3,
    core
)


class AwsVpcPracticeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "mitakeeybucket")
       # queue = sqs.Queue(
        #    self, "AwsVpcPracticeQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        # topic = sns.Topic(
        #     self, "AwsVpcPracticeTopic"
        # )

        # topic.add_subscription(subs.SqsSubscription(queue))
