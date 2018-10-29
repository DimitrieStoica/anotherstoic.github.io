
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

## Storage Comparision ##

|                |  Instance Store | EBS | S3 | Glacier |
| ---------------|-----------------| ----|----|---------|
| Average latency| ms              | ms  | ms, sec, min | min, hr |
| Data volume    | 4 Gb - 48 Tb | 1 Gb - 16 Tib | unlimited | unlimited |
| Item           | block storage | block storage | 5 Tb | 40 Tb |
| Request Rate   | very high     | very high | low - very high | low |
| Cost           | ~ EC2 cost | $$ | $ | $ |
| Durability     | low | high | very high | very high |
 Hot -------------------------------------->  Cold 
