# SNS #
- set-up, operate and send notifications to subscribers
- a publisher sends messages to topics they have created or to topics they have permission to publish to 
- no specific destination address in each message <-> a publisher sends a message to the topic
- SNS matches the topic to a list of subscribers who have subscribed to that topic
- subscribers receive all messages published to the topics to which they subscribe, and all subscribers to a topic receive the same messages

## SNS Subscriber Types ##
- emails
- HTTP/HTTPS
- SMS
- SQS
- mobile push messaging
- Lambda

## Characteristics ##
- single published message
- order is not guaranteed
- no recall
- 256 Kb message
