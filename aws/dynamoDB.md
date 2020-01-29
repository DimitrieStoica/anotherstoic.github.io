# DynamoDB #

- fully-managed noSQL database service
- pay for storage and read/write throughput
- does not have a schema - flexible schema
- desgined to be HA - maintains multiple copies of the data across 3 different AZs <=> eventually consistent (reads might be delayed)
- fast performance - reads/writes stay consistent when database size increases
- infinitely scalable with little effort
- supports documents and key-value data structures
- supports event-driven programming and fine-grained access control
- partition key & / || sort key (if used both sort key needs to be unique)
   
## Read/Write Consistency ##
- 3 facilities -> write to 2 facilities and async to the 3rd one
- eventual consistent 
- strongly consistent - more expensive - read from the master facility
- transactional = ACID consistency - example: insert data at the same time in multiple tables

## DynamoDb Drawbacks ##
- eventually consistent - does not follow ACID properties
- no flexible query language - queries via API calls ( Managing Tables/ Reading Data/ Modifying Data)
- limited data types
- 400 KB maximul items size
- 10 indexes per table
- performance limited to provisioned throughput level (throughput can be modified at any time ~ a couple of minutes)

> composit primary key = partition key + sort key = unique identifier
> the sort key can be used to get the data in order

## Provisioned Throughput ##
- capacity needs to be reserved for I/O, but DynamoDB automatically allocate more space as the table grows
- requests execind capacity unit are throttled and denied with error `privision throughput exceeded exception`

> DynamoDB Auto Scaling is enabled by default (CloudWatch continuously monitors DynamoDB) -> automatically adjusts read and write throughput capacity, in response to dynamically changing request volumes, with zero downtime

> if RCU or WCU are going over the limit set -> DynamoDB will throttle requests

> RCU & WCU is a metric in Cloud Watch

Read Capacity Units (RCU):
- one item
- item size < 4KB
- strong consistency
- per second

> Larger records cost 1 RCU for every 4KB of data (these round up)
> Eventually consistent reads cost half as much (can be specified per querry)

Write Capacity Units (WCU):
- one item
- item size < 1KB
- per second

> Larger records cost 1 WCU for every 1KB of data (these round up)

`RCU and WCU is set when creating a DynamoDB table`

## Queries ##
- searches the table for `a single partition key`
- on a table with only a partition key - query will return at most 1 item
- on a table with a compound key - query will return all records matching the partition key
- queries can be limited to a range of sort keys
- queries can be strongly consistent or eventually consistent
- results can be filtered on any attributes or ordered by sort key

> a filter cost 1 RCU
> a querry needs to be narrowed down to a single partition key => a filter will cost nr. of narrowed down results RCU's

## Scans ##
- searches the table across `all partition keys`
- scans can be filtered by attributes
- scans cannot be ordered
- scans are always eventually consistent
- scans can be run in parallel

> filtered scans are expensive and slow because DynamoDB needs to reads every single record and compare it with the filter => 1 RCU per read line

## Secondary Indexes ##
- define an index to access data with a different condition
- additional indexes to write querries and search data by other attributes
- each querry can work only one 1 index
- compared with scan, Secondary Indexe use less RCU's because "filtering" is done through the index

> for local - partition key is the same and only secondary changes <=> synchronous

> for global - partition key & secondary are different <=> synchronous

### Global Secondary Indexes ##
- query across the entire table
- projects a table by re-keying with the required attributes: partition key || sort key
- Global Secondary Indexes require storage space and configuring provisioned throughput
- a query on an attribute will return the attribute and the partition key, but if we want the rest of the attributes we need a projection

> by default all atributes into the table are projected into the index = returns retrieve all attributes => cost >> WCU/RCU and space
> attributes in Global Secondary Indexes can be specified
> Global Secondary Indexes can have sort keys

- materialized projection - read only - you can't write in a secondary index => changes are propagated from the main table 
- no key constraints in the projection - multiple replies
- if attribute is null the item won't appear in the secondary index - sparse projection
- there is a propagation time between base table and secondary - no consistent read
 
 > if all attributes are projected: WCU on the main table = WCU on GSI table while RCU can vary on load
 - can be created with the table or later
 - throughput is allocated separetly for each GSI
 - limit to 5 GSIs per table
 
### Local Secondary Indexes ###
- query within a single partition key
- not useful if table doesn't have a compound key
- used when filters are expensive actions

- the secondary table is on top of the base one - no propagation time

- must be created when the table is created
- throughput is shared with the main table
- limit to 5 LSIs per table

> similar to Global Secondary Indexes. However, the Local Secondary Indexes partition key must be the same with the table's partition key

## Partitions ##
- when a table gets too large (> 10 Gb or when RCU's + WCU's > X value): DynamoDB splits the table in partitions
- primary key = partition key = hash keys
- partition key is used to determine which partition an item should be stored in
- DynamoDB knows how to map partition keys to the physical partitions

> for a table with a compound key all records with the same partition key are stored in the same DynamoDB server

> nr. of partitions = max(Table size/10 Gb, (RCU/3000 + wCU/1000))

> in `bulk reads/writes` the table might be split into more partitions than what's expected ( ex. 10.1 ~ 11 )

- natural growth of data size is a power of 2
- each partition will have half of the partition key space

> DynamoDB uses a hash algorithm to choose which partition data belongs to

## Performance ##
- when a table is split into partitions Provisioned Throughput is equally split across partitions 

> Throughput per Partition = Total Provisioned Throughput / Partitions

- performance problems become obvious when some partitions are much larger than the others and RCU's and WCU's are only a proportion of the total Provisioned Throughput 

> choose a partition key that ensures data will be balanced: 

    Streams
        once a change occured to a table, DynamoDb Stream writes async update to a stream -> trigger events

    Global Tables
        global replication recorded in the stream and replicated across regions
        consistent reads available only in the region the event was updates - no consistent reads in the other region
        last write wins

    Conditional Write Operations
        dynamoDb won't charge for operations if conditional = true
        non atomic test and set - optimistic locking with version number

## Streams ##
- read each action to DynamoDB with a DynamoDB Stream and react to ations => event driven architecture
- data on the stream is configurable => item 

## Data Replication ##
- replicate cross region with streams
- race conditions for propagatin data - fixed with metadata time = last one wins 

> use case: active - active 

## Back up & Restore ##
- full back up, restore, point-in-time recovery (part of the table)
