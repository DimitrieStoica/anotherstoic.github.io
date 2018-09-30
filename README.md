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

# AWS Storage Fundamentals #

## Ephemeral ##
- temporarily, local storage 
- automatically attached to every instance - page file, swap file

## EBS ##
- provides block level storage to EC2 insntaces
- offers persistent and durable data storage - used to retain valuable data
- it can exist without being attached to an instances - operates as a seperate service
- it can't be attached attached to more than one instance at a time
- it can be transferred between AZ's
- EBS volume data is replicated across multiple servers in the same AZ
- allos encryption of data, boot volumes & snapshots
- designed for an annual failure rate (AFR) 0.1% - 0.2% & SLA 99.95%
- EBS volumes are elastically scalable - the file system needs on the OS needs to be extended to see the new volume

- Volume Types:
 * default volume for EC2: GP-SSD (General Purpose SSD) - system boot volumes, small to medium DB's
 * PIOPS (Provisioned IOPS) - SSD based, I/O intensive, NoSQL/Relational DB's
 * Throughput Optimized HDD - infrequent data access, cannot be a boot volume, big Data & log processing
 * Cold HDD - large volumes of data, lowest storage cost, cannot be a boot volume
 * Magnetic - infrequent data access

> RAID - is a data storage virtualization technology that combines multiple physical disk drive components into one or more logical units for the purposes of data redundancy, performance improvement, or both. RAID is a function of the guest OS. 

> IOPS (Input/output operations per second): Size(GiB) ration 1:50

Snapshots:
- point-in-time snapshots
- supports incremental snapshots - each snapshot will only copy data that changed from previous snapshot (billed only for the changed) blocks
- deleting a snapshots removes only the data not needed by any other snapshots
- EBS stores snapshots in S3
- it can be used to resize EBS volumes
- EBS volumes can be shared or used across regions

Encryption:
- EBS ofers managed encryption at rest and in transit
- AES-256 with KMS (CMK/DEK)
- snapshots will also be encrypted

Pricing:
- priced for the amount of storage provisioned

> Anti-patterns: temporary storage, multi-instance storage access, very high durability and availability

## EFS ##
- network attached storage (~ NFS)
- simple, petabytes scalable file storage
- elastic sizing based on adding/removing files
- data is replicated across multiple AZs
- supports multiple connections concurently 
- use cases: Big Data, analytics, media processing, content management
- connect via direct connect as well

## S3 ##
- S3 is a fully managed object storage based system: `Highly Available`, `Highly durable`, `Highly scalable` & `cost effective`
- file size supported: 0 bytes - 5 terabytes
- objects stored in S3 have a `durability` of 11 9's as data is replicated across multiple AZs

> Durability: the probability of maintaining your data without it being lost, corruption, degradation of data

- the `availability` of S3 data objects is 4 9's

> Availability: Up time of the service maintaining your data

Buckets:
- data is stored in S3 buckets as objects accessible via HTTP/HTTS
- bucket names must be globally unique, buckets are regional based
- default: <100 buckets per AWS account
- names up to 63 characters, only lower case, no period character (bucket name converts to a subdomain when using "." that can't be used with SSL) - bucket name gets converted into DNS
- can be versioned enabled
- allows cross regional replication

Storage Classes:
- Standard: 11 9's Durability, 4 9's Availability
- Standard-Infrequent Access: 11 9's Durability, 3 9's Availability
- Reduced Reduced Redundancy: 4 9's Durability, 4 9's Availability

Security:
- Bucket policies: set access controls for accesing data in the bucket associated with - permissions for AWS users
- Access Control Lists: only control access from users outside the AWS account - public access
- Data Encryption: server side encryption/ client side encryption

Data management:
- Versioning: 
  * allows multiple versions of the same object to exist
  * recover from accidental deletion
  * versioning is not enabled by default
  * once enabled, versioning can't be disabled - only suspended
  * adds a cost for storing multiple versions of the same object
- Lifesycle rules:
  * provides an automatic method of managing the lifecycle of your data stored - move data between storage classes

Use cases:
- data backup - for existing AWS services/ on-premises data
- static content & websites
- large data sets (computational, mathematical & scientific data)
- integration with EBS (store snapshots), CloudTrail (log files are stored in S3), CloudFront (S3 bucket can be used as a CloudFront origin within a distribution)

Pricing:
- the more storage used, the cost of eeach Gb reduces when a certain treshold is reached
- others costs: requests (based on actions: PUT, GET, COPY, POST), data transfers

Anti-patterns:
- data archiving for long term use
- dynamic & fast changing data
- file system requirements
- structured data with queries

- key in S3 = path 
- version enabled files needs to be all individually deleted (including versions)
- encryption in transit HTTPS
- encryption at rest
- CORS needs to be configured to a bucket

Operations on Objects: PUT, GET, LIST keys, DELETE, RESTORE (restore an object previosuly archived on Glacier)

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
