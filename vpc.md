## Virtual Private Cloud - VPC ##

- first logical foundation that allows you to create/deploy/configure services & instances
- logically isolated network in the AWS cloud - private CIDR block of AWS cloud
- a VPC is region wide -> use all available AZs
- the size of a VPC cannot be changed
- consists of: subnets, route tables, internet gateways, elastic IPs, endpoints, NAT gateways, peering connections, network ACLs, security groups, VPN

> the default limit of route tables allowed per VPC is 200.

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

`Security zoning` is creating a group of system components which have similar security levels and a group of common controls

| Security Groups | Network Access Control Lists |
| --------------- | ---------------------------- |
| operates at the instance level | operates at the subnet level |
| supports only ALLOW rules | supports ALLOW and DENY rules |
| applies to an instance only if associated with an sg | automatically applies to an instance |
| STATEFUL: return traffic allowed is assumed | STATELESS: traffic is strictly filtered, return traffic allowed is not assumed |

> for inbound traffic: Network ACL's are evaluated first followed by security groups rules

> for outbound traffic: Security groups are evaluated first followed by Network ACL's

> the maximum number of security groups per network interface an instance in a VPC can belong to is 5.

## VPC NAT Gateways ##
- allows private instances to get access to the Internet
- scale UP: choose an instance that supports enhanced networking
- scale OUT: add NATs per subnets and distribute workload (1 Subnet = 1 NAT)
- HA by failing over to another NAT
- default limit for NAT gateways per Availability Zone is 5

> a NAT gateway in the pending, active, or deleting state counts against your limit

## Endpoints ##
- when trying to access services like S3 communication happens over the internet
- to keep the traffic localized (security/regulatory/performance) you can deploy an endpoint and route traffic from subnet to a service

## VPC Peering ##
- network connection between 2 or more VPC's in the same region - same AWS account or different AWS account
- uses private IP addresses
- up to 50 VPC Peering connections
- enables the routing using each other VPC's private IP address -> no overlapping IP address ranges
- there is no single point of failure or network bandwidth bottleneck between the VPCs

> expiry time for an unaccepted VPC peering connection request is 1 week (168 hours)

## VPN Connectivity ##
- a VPN connection refers to the connection between your VPC and your own network

> Virtual Private Gateway: the anchor on the AWS side of the VPN connection

> if a VPN connection have been compromised, you can change the IKE preshared key

> VPN connection-hours are billed for any time your VPN connections are in the "available" state

### Corporate or home network to Amazon VPC ###
- extend network to AWS -> use AWS services seamlessly
- no overlapping IP ranges

+ Hardware based IpSec VPN over the Internet
+ Direct Connect with VPN: 1 or 10 10 gigabit link
+ Software based VPN over the Internet: fully customer managed -> need to manage HA
+ VPN Cloud Hub: hub and spoke mode between a hardware VPN and direct connect option (Amazon VPC, virtual private gateway, with multiple customer gateways) that allows multiple VPN

### Amazon VPC to Amazon VPC ###
+ VPC peering
+ software-based VPNs. In this configuration, you need to have an internet gateway at both VPCs to enable communication between the software-based VPN appliances, fully customer managed -> need to manage HA
+ hardware based IPSEC VPN connection between VPC's
+ VPC to VPC over direct connect

### End user to VPC ###
+ corporate home network to the VPC
+ software remote access VPN

## VPC Scenarios ##
- VPC with single public subnet
- VPC with public and private subnet
- VPC with public and private subnets and a hardware of VPN access
- VPC with private subnet only and hardware VPN access

> the hotplug script that is part of ec2-net-utils used with ENIs generates an interface configuration file suitable for use with DHCP

> a set of DHCP options can't be modified -> create a new set of DHCP and associate them with your VPC

## Elastic network interface (ENI) ##
- a virtual network interface that you can attach to an instance in a VPC
- it can include: one public IP address, a MAC address,  source/destination check flag, a description, a primary private IP address, one or more secondary private IP addresses, one Elastic IP address per private IP address
