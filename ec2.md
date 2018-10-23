# EC2 #
- allows to deploy virtual servers

`placement groups` enable applications to get the full-bisection bandwidth and low-latency network performance required for tightly coupled, node-to-node communication typical of HPC applications.

> The EC2Config service is started when the instance is booted. It performs tasks during initial instance startup and each time you stop and start the instance.

## Amazon Machine Images ##
- template of pre-configured EC2 instances
- includes operating system, applications and any custom configuration

> AMI characteristics: Region, Operating system, Architecture (32-bit or 64-bit), Launch Permissions, Storage for the Root Device
> When the EC2 instance is launched from an instance store backed AMI, it will not allow the user to configure the shutdown behaviour to “Stop”. It gives a warning that the instance does not have the EBS root volume.

## Instance types ##
- varied rage of CPU, memory, storage, and networking performance
- general purpose <-> balance mix of CPU, memory, storage
- compute optimized <-> high performance processors
- GPU
- memory optimized <-> in memory applications
- storage optimized <-> SSD backed storage

> CPU credits govern the baseline performance of Burstable Performance Instances 
> Accelerated computing instances enable more parallelism for higher throughput on compute-intensive workloads - Graphics Processing Units (GPUs) or Field Programmable Gate Arrays (FPGAs)

## Instance purchasing options ##
- on-demand instances: used for short, irregular workloads
- reserved instances: purchase an instance type for a set period of time in return for a reduced cost compared to on-demand
- spot instances: bid for unused EC2 compute resources
- dedicated instances
- dedicated hosts: similar to dedicated instances, however, they offer additional visibility and control over how instances are placed on the physical host

> two-minute warning before the spot instance is automatically terminated 

## Tenancy ##
`Shared tenancy`- other customers and users have EC2 instances running on the same host
`Dedicated tenancy` - instances hosted on hardware that no other customer can access

## User data ##
- commands that will run during the first boot cycle

## Storage options ##
- EBS volumes -> persistent storage
- instance store volumes -> ephemeral storage

> ephemeral storage is available for EBS backed AMIs provided the instance size is not micro

> ECC memory is necessary for server infrastructure, and all the hardware underlying Amazon EC2 uses ECC memory

## Security ##
- security groups
- key pairs

## Pricing ##
- when an EC2 dedicated instance is stopped, you are charged a full instance hour for volume storage for every transition from a stopped state to a running state
