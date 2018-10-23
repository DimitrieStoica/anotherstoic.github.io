# aws-certification-study-notes
AWS Certification Study Notes

- the WebUI, CLI or SDK are all used to interract with the AWS API

### Best Practices: Developing Cloud Apps ###
- loosely coupled apps 
- arhitect for resilience; design for failure
- log metrics and monitor performance
- security in every layer

## Auto Scaling ##
- decrease, increase resources based on demand (rules & metrics)
- bootstrap and dynamic configuration for provisioning software on new instances
- integrates with CloudWatch (ex: if CPU >= 90%)
- manual scheduled configuration (min || max values, time and date)
- notifications (SQS, SNS)
- it is free
- Auto Scaling group defines the capacity of the group and where the group should place resources 
- Launch Configuration is a template used to launch new instances: AMI, instance type, spot instances, user data, storage configiguration
- Scaling Plans - triggers, how to deal with provisioning/ terminating instances

## Elastic Beanstalk ##
- install, distribute, maintain applications via cluster of EC2 instances: web applications or worker environemnt
- the service is free but any resources that are instanciated are payed for (EC2, ELB)
- Elastic Beanstalk arhitecture:
  * Applications: collectio of environment vars, configurations, app versions
  * Application Versions: a specific reference to a section of deployable code usually stored in S3
  * Environemnt: An application version deployed in AWS
  * Environemnt Configuration: collection of params and settings on how AWS resources will behave
  * Configuration Template: baseline for creating AWS resources
- workflow: create application, upload application version + config, launch environment, manage environment (update to new versions)

## AWS Lambda ##
- serverless computer service = manage function execution
- no inbound connections are blocked
- only TCP/IP
- p-trace (debugging) are restricted
- all calls limited to 5 min
- Lambda functions can be executed on a regular schedule
- attach Lambdas to an URL with API Gateway

## Step Functions ##
- define a state machine (workflow)

## SQS ##
- pulling messaging service

- FIFO mode - preservsorder, slower, rate limited 300 transactions / second, recommended to use only one single process reading from the queue
- standard mode - best effort ordering, messages may be duplicated, throughput nearly unlimited, processes need to work well with duplicates
- push messages into the queue as a producer, consumer consumes the message and deletes it or pushes it back if it doesn't know what to do
- short poll: non blocking poll - hits only a subset of nodes
- long poll: tries it's best to return one messag, if there is anything - sample all of the nodes

## SNS ##
- push messaging service

Use Case: Fan-Out

## Kinesis ##
- no message deletion, a record stays until the retention window
- the partition key is used to determine which shard
- manage partitions and shards explicitly

## IAM ##
- centrally manage users and users permissions in AWS
- create users, groups, roles and policies

## Cloud Watch ##
- monitoring service
- takes as input metrics and generates logs
- gives log aggregation capabilities
