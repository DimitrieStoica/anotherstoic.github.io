# Amazon CloudFront #

- content delivery network that speeds up the distribution of static and dynamic content via a worldwide netowrk of edge locations
- pricing is based on data transfer out to the internet and to the origin + nr. of HTTP/HTTPS requests

> Invalidation Requests: TTL at edge locations

> SSL: dedicated IP Custom SSL

There are 5 key reports:
- cache statistics
- Ppopular objects
- top referrers
- usage report
- viewers report

## Best Practices ##

Static Assets: 
- use S3 (CloudFront trasfers to S3 is free)
- Control Access to Content on S3
- Contrl Access to Content on CloudFront
- edge caching
- versioning

Dynamic Assets:
- cache everything (TTL >= 0 seconds)
- use multiple cache behaviors: avoid forwarding cookies and User-Agent Header

Streaming Media:
- low TTL for manifest file
- highTTL for Media Files
- HTTP based streaming

Arhitectural Consderations:
- Route 53 for Health Checks
- enable HTTPS
- Cloud Watch for Alarms and Notifications
