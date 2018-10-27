# EC2 #
- allows to deploy virtual servers

`placement groups` enable applications to get the full-bisection bandwidth and low-latency network performance required for tightly coupled, node-to-node communication typical of HPC applications.

> the EC2Config service is started when the instance is booted. It performs tasks during initial instance startup and each time you stop and start the instance

Enhanced networking enables:
- more packets per second
- lower latency
- less jitter

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

> with reserved instances you can change the instance type within the same instance family and you can change the AZ

- spot instances: bid for unused EC2 compute resources

> two-minute warning before the spot instance is automatically terminated 

- dedicated instances

> dedicated instances may launch on any hardware allocated to the customer

- dedicated hosts: similar to dedicated instances, however, they offer additional visibility and control over how instances are placed on the physical host

>  dedicated hosts allow usage of existing server-bound software licenses

`reserved instances`- best value for a steady traffic over an extended period

`on-demand instances`- perfect for handling short term traffic spikes

`spot instances` - best value for non-critical applications that can afford to be stopped

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

> a STOP/RESTART of an EBS-backed EC2 always changes the underlying host computer

## Security ##
- security groups
- key pairs

## Pricing ##
- when an EC2 dedicated instance is stopped, you are charged a full instance hour for volume storage for every transition from a stopped state to a running state

## Elastic IP ##
- remains with an instance when the instance is stopped 
- if an EIP is attached to an instance that is associated to a different subnet -> instance will be dual-homed

## Limitations ##
- key-pairs: 5000
- reserved instances: 20 per AZ per month
- AMI copies: 50 at a time, no more than 20 coming from a single source region

