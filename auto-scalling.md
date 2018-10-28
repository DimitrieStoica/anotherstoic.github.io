
# Auto Scaling #

- free service that decreases, increases resources based on demand (rules & metrics)

> ELB only checks the health of an instance. If unhealthy they will stop routing traffic to it. They do not terminate the instance

- used to create steady state workloads that need a consistent number of EC2 instances - auto scale and monitor
- manual scheduled configuration based on predictive traffic patterns (min || max values, time and date)
- notifications to SQS, SNS
- Launch Configuration is a template used to launch new instances
- Scaling Plans - triggers, how to deal with provisioning/ terminating instances

- integrates with CloudWatch (ex: if CPU >= 90%)

> by default detailed CloudWatch monitoring is enabled for Auto Scaling

## Auto Scaling elements ##
- minimum size
- launch configuration
- (optional) health checks and desired capacity

## Launch configuration elements ##
- AMI
- instance type
- (optional) key pair, the security group, and the blocked device mapping

## Limits ##
- 100 launch configurations per region
- 20 EC2 instances perregion

## Methods ##
- Launch: adds a new EC2 instance
- Terminate: remove an EC2 instance
- Healthcheck: checks the health of an instance if told by EC2 or ELB
- ReplaceUnhealthy: termintes unhealthy instances and replaces it with a healthy one
- AZRebalance: balances the number of EC2 instances in the group across the AZ's in the region (unhealthy AZ)

> if AZ becomes unhealthy Auto Scaling will `first` launch new instances in the unaffected AZ before terminating unhealthy EC2's <-> if terminate process is suspended => this will result in a larger Autos Scalling group

- AlarmNotification - accepts notifications from CloudWatch associated with the group -> it won't be able to perfrom actions that involve creating/terminating instances
- AddToLoadBalaner - adds instance to ELB target group

