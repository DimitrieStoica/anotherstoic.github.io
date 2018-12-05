## RTO/RPO ##

`Recovery Time Objective (RTO)`: the time it takes after a disruption to restore a business process to its service level as defined by its operator level agreement

`Recovery Point Objective (RPO)`: the maximum allowable threshold for data loss measured in time 

## Disaster Recovery ##

| | Back up & restore | Pilot light | Warm stand by | Multi site |
|-|-------------------|-------------| --------------|------------|
| Description |data is stored as a virtual tape library| min version of env that can easily extended | scaled down version of a fully func env | fully operational version                    |
| RTO | high | lower than back up & restore | lower than pilot light as partially running  | lowest |
| RPO | since the last back-up | since the last snap-shot | since the last data write if M/S multi AZ DB | since the last data write if M/S multi AZ DB |
| Cost | low | low | medium | high |
