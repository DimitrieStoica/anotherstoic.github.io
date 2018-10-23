## Virtual Private Cloud - VPC ##

- first logical foundation that allows you to create/deploy/configure services & instances
- logically isolated network in the AWS cloud - private CIDR block of AWS cloud
- a VPC is region wide -> use all available AZs
- the size of a VPC cannot be changed
- consists of: subnets, route tables, internet gateways, elastic IPs, endpoints, NAT gateways, peering connections, network ACLs, security groups, VPN

> Default VPC: logically isolated network with a default subnet, security group and an Internet Gateway -> any instance will automatically receive public IP address

### Pricing ###
- there are no charges for creating and using a VPC <-> accessing AWS resources via your VPC internet gateway is free
- VPN connections and data transfer are charged (pair per hour basis)
- no charge for creating a VPC peering connection <->  data transfer across the peering connection is charged
- no charge for using classic link <-> data transfer across availability zones is charged

## VPC Core Components ##

### Subnets ###
- are CIDR blocks within the IP range of your VPC, there can be one or more subnets in a VPC
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
- netmask between CIDR 16-28
- each subnet must be associated with a Route table and a Network Access Control List

### Internet Gateway - IGW ###
- provides connectivity in and out of the VPC
- provides a target in the VPC route table for Internet-routable traffic
- performs network address translation for instances that have been assigned public IP addresses
- if a subnet is associated with a route table that has a route to an Internet gateway = `public subnet`

### Direct Connect ###
- private dedicated connection between VPC and on prem

## VPC Security ##

| Security Groups | Network Access Control Lists |
| --------------- | ---------------------------- |
| operates at the instance level | operates at the subnet level |
| supports only ALLOW rules | supports ALLOW and DENY rules |
| applies to an instance only if associated with an sg | automatically applies to an instance |
| STATEFUL: return traffic allowed is assumed | STATELESS: traffic is strictly filtered, return traffic allowed is not assumed |

> For inbound traffic: Network ACL's are evaluated first followed by security groups rules

> For outbound traffic: Security groups are evaluated first followed by Network ACL's

## VPC NAT Gateways ##
- allows private instances to get access to the Internet
- scale UP: choose an instance that supports enhanced networking
- scale OUT: add NATs per subnets and distribute workload (1 Subnet = 1 NAT)
- HA by failing over to another NAT

## Endpoints ##
- when trying to access services like S3 communication happens over the internet
- to keep the traffic localized (security/regulatory/performance) you can deploy an endpoint and route traffic from subnet to a service
