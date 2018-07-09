# aws-certification-study-notes
AWS Certification Study Notes

- the WebUI, CLI or SDK are all used to interract with the AWS API

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

## EC2 ##
- one of the only services that is not HA

### Best Practices: Developing Cloud Apps ###
- loosely coupled apps 
- arhitect for resilience; design for failure
- log metrics and monitor performance
- security in every layer

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


