# aws-certification-study-notes
AWS Certification Study Notes

- the WebUI, CLI or SDK are all used to interract with the AWS API

### Best Practices: Developing Cloud Apps ###
- loosely coupled apps 
- arhitect for resilience; design for failure
- log metrics and monitor performance
- security in every layer

## 1. VPC - Virtual Private Cloud ##
- first logical foundation that allows you to create/deploy/configure services & instances
- logical isolated network in the AWS cloud
- consists of: subnets, route tables, internet gateways, elastic IPs, endpoints, NAT gateways, peering connections, network ACLs, security groups, VPN
- a VPC is region wide -> use all available AZs (a router allows all subnets within a region across the AZs that in the same region to be interconnected across the region)

### VPC characteristics ###
- 5 IPs reserved/subnet (first 4 and last 1). For example, in a subnet with CIDR block 172.0.0.0/24, the following five IP addresses are reserved:
  * 172.0.0.0: Network address
  * 172.0.0.1: Reserved by AWS for the VPC router
  * 172.0.0.2: Reserved by AWS for the DNS server
  * 172.0.0.3: Reserved by AWS for future use
  * 172.0.0.255: Network broadcast address
- Subnets:
  * private: DBs, Application Servers, File Servers
  * public: Web Servers, NAT, VPN
  * VPN dedicated
- Subnets do not span across AZs
- CIDR 16-28
- Select IP prefix

### VPC Security ###

Security Groups  | Access Control Lists
---------------- | --------------------
apply at the resource level: instances, ELBs  | source & protocol fintering
control Ingress/Egress traffic | subnet level traffic protocol, separate inbound/outbound rules
stateful: return traffic allowed is assumed | stateless: traffic is striclty filtered, return traffic allowed is not assumed

### VPC NAT Gateways ###
- allows private instances to get access to the Internet
- scale UP: choose an instance that supports enchanced networking
- scale OUT: add NATs/ subnets and dristribute workload (1 Subnet = 1 NAT)
- HA by failing over to another NAT

### Endpoints ###
- when trying to access services like S3 communication happens over the internet
- to keep the traffic localized (security/regulatory/performance) you can deploy an endpoint and route traffic from subnet to a service

# AWS Compute Fundamentals #
## EC2 ##
- one of the only services that is not HA

## ELB ##
- direct and route traffic across a fleet of EC2's = maintain HA and Resiliency
- distributes requests accross all servers and across multiple AZ's (at least 2)
 * Classic Load Balancing:
  - routes traffic based on application and traffic information
 * Application Load Balancing:
  - routes traffic at an advanced application level
- internal LB - internal IP address, accessed only from the internal network 
- external LB - public IP address
- ELB Listeners check for connection requests over HTTP, HTTPS, TCP & SSL
- Health Check monitors the health of any instance associated to any ELB by permorming a ping
- If a response in not received after TTL expired the instance will be noted as unhealty and traffic will not be routed to that instance

## Auto Scaling ##
- decrease, increase resources based on demand & load balance traffic evently across multiple instances 
- Launch Configuration is a template used to launch new instances: AMI, instance type, spot instances, user data, storage configiguration
- Auto Scaling group defines the capacity of the group and where the group should place resources 

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

## S3 ##
- generic storage, similar to a file store
- data is stored in S3 buckets as objects via HTTP
- buckets:
  * names must be globally unique
  * names up to 63 characters, only lower case, no period character (bucket name converts to a subdomain when using "." that can't be used with SSL) - bucket name gets converted into DNS
  * can be versioned enabled
  * allows cross regional replication
- key in S3 = path 
- version enabled files needs to be all individually deleted (including versions)
- encryption in transit HTTPS
- encryption at rest
- CORS needs to be configured to a bucket

Operations on Objects: PUT
- upload object
- single upload S3 object <= 5GB
- multipart upload - recommended if size > 100 Mb

Operations on Objects: GET
- get range of bytes
- get complete object

Operations on Objects: LIST keys

Operations on Objects: DELETE

Operations on Objects: RESTORE
- restores an object previosuly archived on Glacier


Performance (https://minops.com/blog/2015/01/aws-s3-performance-tuning/)
- Throughput
  * S3 takes the first few characters of the key and decides which cluster partition to put them in
  * > 3k transactions per second generate a hash prefix for the key

- Requests
  * avoid unnecessary requests: do not check for the existance of a bucket

- Network Latency
  * CDN in front of S3 to distribute content
  * choose the region closest to low latency client
  
  Best pracitices:
  - separate input/output buckets

## DynamoDB ##
- noSQL database service
- does not have a schema
- supports documents and key-value data structures
- supports event-driven programming and fine-grained access control
- used when accessed with end user applications (responsivness over corectness)
- partition key & / || sort key (if used both sort key needs to be unique)
- pay for how much you store, read/write throughput
- maintains multiple copies of the data for durability - eventually consistent (reads might be delayed)

Performance
- read & write throughput: Read Capacity Units (items < 4KB) and Write Capacity Units ( items < 1KB)
- Throughput per Partition = Total Provisioned Throughput / Partitions
- Performance problems:
  * data distribution - table too heterogenous 
  * data access pattern - enforce single partition access
  
  Getting data out of DynamoDB:
  - scan
  - querry
  
  Global Secondary Index:
  - projects a database by re-keying with the required attributes: partition key || sort key
  - materialized projection - read only - you can't write in a secondary index (changes are propagated from the main table - still pay for WCU)
  - no key constraints in the projection - multiple replies
  - if attribute is null the item won't appear in the secondary index - sparse projection
  - there is a propagation time between base table and secondary - no consistent read
  
  Local Secondary Index
  - use different key for only the sort key
  - local = non materialized projection (share the Throughput of the base table)
  - the secondary table is on top of the base one - no propagation time
  
  Streams
  - once a change occured to a table, DynamoDb Stream writes async update to a stream -> trigger events
  
  Global Tables
  - global replication recorded in the stream and replicated across regions
  - consistent reads available only in the region the event was updates - no consistent reads in the other region
  - last write wins
  
  Conditional Write Operations
  - dynamoDb won't charge for operations if conditional = true
  - non atomic test and set - optimistic locking with version number

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
