# Replay-Access-Log

The purpose of the tool is to replay a traffic pattern from given server access log (Apache or NGINX) on a specified server ip address.  While replaying the traffic, the tool maintains the following:- 
1. Replay the transactions, identical to the inter request times in the access log.
2. Replay the clients, (since the source ip is fixed) by utilising different ports for different clients.
3. Also if the server sends any cookie of a client, the cookie is sent in the  subsequent requests for that client.