# Route 53 #
- AWS DNS service

> DNS = translates domain names into IP addresses (port 53)

`hosted zone` = collection of resource record sets hosted by Route 53. Like a traditional DNS zone file, a hosted zone represents a collection of resource record sets that are managed together under a single domain name

- the name of each resource record set in a hosted zone must end with the name of the hosted zone. For example, the example.com hosted zone can contain resource record sets for www.example.com and accounting.tokyo.example.com subdomains, but cannot contain resource record sets for a www.example.ca subdomain

## Routing types ##
### Simple routing (round robin) ###
- uses a simple routing policy when you have a single resource that performs a given function for your domain
- example: the IP address in an A record

### Weighted round robin ###
- allows you to assign weights to resource record sets in order to specify the frequency with which different responses are served
- A/B testing

### Latency-based routing (LBR) ###
 - improves application’s performance for a global audience
 - routes clients based on actual performance measurements of the different
 
 ### Geolocation routing ###
- allows routing based on the geographic location of your users

### Geoproximity routing ###
- allows routing traffic based on the physical distance between your users and resources

### Multiple answers ###
- route traffic approximately randomly to multiple resources

## DNS failover ##
- Amazon Route 53 can help detect an outage of your website and redirect your end users to alternate locations

> String Matching: the health check looks for a particular string in the page body 
