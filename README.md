# aws-certification-study-notes
AWS Certification Study Notes

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
