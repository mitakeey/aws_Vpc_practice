#!/usr/bin/env python3

import aws_cdk as cdk

from aws_vpc_practice.aws_vpc_practice_stack import AwsVpcPracticeStack


app = cdk.App()
AwsVpcPracticeStack(app, "aws-vpc-practice")

app.synth()
