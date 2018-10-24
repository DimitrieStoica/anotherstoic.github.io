# Elastic Load Balancer - ELB #

- directs and routes traffic across a fleet of EC2's to `maintain HA and Resiliency`
- distributes requests across all servers and across multiple AZ's (recommended to use at least 2) - region wide load balancers
- `internal LB` - internal IP address, accessed only from the internal network 
- `external LB` - public IP address
- ELB does not terminate or start instances, but it detects the health of an instance

> it monitors the health of any instance associated to any ELB by performing a ping. If a response in not received after TTL expired the instance will be noted as unhealthy and traffic will not be routed to that instance

- supports sticky sessions using cookies - traffic is routed to the same instances as the user continues to access an application
- enables SSL offloading and supports SSL termination

## TLS termination Elastic ##
Load Balancing provides integrated certificate management and SSL decryption, allowing you the flexibility to centrally manage the SSL settings of the load balancer and offload CPU intensive work from your application.

## ELB types ##

### Classic Load Balancing ###
- Layer 4 and Layer 7 LB - SSL termination and processing (results in better performance for EC2's)
- cookie-based sticky sessions
- it can be integrated with Cloud Watch to build advanced metric load balancing (CPU, memory) and not just Round Robin 
- it can be integrated with Route 53 for DNS load balancing (multiple ELB's across multiple regions)
- supported ports: `25 (SMTP), 80/443 (HTTP/HTTPS), 1024-65535`
- supports IPv4 and IPv6
- only `1 SSL certificate/ELB`, but wildcard certificates are supported
- does not support EIP - it only works with DNS
- supports domain Zone Apex (no need to use www. )
- integrates with Cloud Trail for log security analysis
- check for connection requests over HTTP, HTTPS, TCP & SSL
  
    > Cross-Zone Load Balancing: when enabled the LB probes the instances that are within the AZ and will load balance traffic against this instances. If unchecked it treats the AZ as a single instance disregarding instances within
    
    > Connection Draining timeout: when an instance is taken out of rotation, it can be immediately disconnected or slowly drained the connections out
  
### Application Load Balancing ###
- protocol oriented LB - operates at the request level = Layer 7 only
- supports path-based routing and host-based routing
- supports microservices and containers (it can dynamically map container ports)
- better performance for streaming
- reduced cost
- deletion protection - instance can't be deleted until deletion protection is deleted
- better Health Checks and Cloud Watch metrics
- check for connection requests over HTTP, HTTPS
- supports `sockets, path based routing & HTTPv2` 
  
 ### Network Load Balancer ###
 - simple LB designed to handle sudden and volatile traffic patterns - TCP traffic
 - no need to be pre-warmed
 - operates at Layer 4
 - single static IP address per AZ
 - targets: EC2 instances, ECS, IP address
 - supports static and elastic IP addresses
 - can load balances across multiple ports on an instance
 
 ### What ELB type to use ###
 - support static or elastic IP address: Network LB
 - control over SSL cipher: Classic LB
 - container services or ECS: Application LB or Network LB
 - support SSL offloading: Application LB or Classic LB
 
- Listeners: 
  - define the port and the protocol
  - each ALB needs 1 Listener and up to 10 Listeners
  - routing rules are defined on listeners
  
- Target Groups:
  - logical grouping of targets for the LB
  - accepts EC2, containers - it can't be mixed and match in the same target group
  - can exist independently from the LB
  - region based but can be associated auto scaling group
  - up to 100 instances
  
- Rules: 
  - each Listener can have 1 or more rules for routing requests to a target group
  - consists of _conditions_ & _actions_: when a request meets the condition, an action is taken
  - if a request comes in that doesn't meet any of the conditions, it will use the default rule and sends it to the default target group
  
- Health Checks:
  - ALB's allow custom response codes (200-399)
  - ALB's provide detailed health check failures
  - detailed access log information delivered to an S3 bucket indexed by date
