# RDS #

## Scale RDS ##
- scale up/down with resizable instance types
- offload read traffic to Read Replicas
- put a cache in front of RDS (example: ElasticCache)

### Scaling RDS Writes with Database Sharding ###
- without shards, all data resides in one partition
- with shards, data is split into large chunks (shards) -> better performance & better operating efficiency

### Horizontal scaling with Read Replicas ###
- add a Read Replica to: offload reporting & horizontal scale for read-heavy workloads

> Read Replicas are async

### Scaling RDS ###
- scale the compute and memory resources powering a deployment up or down
- there is minimal downtime when scaling up on a Multi-AZ environment because the standby database gets upgraded first, then a failover will occur to the newly sized database
- a single-AZ instance will be unavailable during the scale operation

