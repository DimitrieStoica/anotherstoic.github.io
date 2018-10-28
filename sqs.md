# SQS #
- fully managed message queueing service
- transmits any volume of messages at any level of throughput

> queue can be shared between multiple AWS accounts or anonymously <-> the queue owner pays for the shared queue

- supports multiple readers & writes on the same queue (repository for messages awaiting procesing == buffer)

> message: 256 Kb of text in any format

## SQS Types##
- standard: at least one delivery & best effort ordering
- FIFO: exaclty-once processing & limited throughput

> SQS allows queuing chain pattern <-> async cloud design patterns that helps achieve loose coupling of systems by using queues between systems and exchanging messages that transfer jobs

## Visibility timeout ##
- prevents multiple components from reading the same message 
- messages are locked while being processed
- the components that receives the message processes it and deletes it from the queue
- the the message processing fails - the lock will expire and the message is available again

> A dead letter queue (DLQ) receives messages after a maximum number of processing attempts has been reached -> provides the ability to isolate messages that could not be processed
