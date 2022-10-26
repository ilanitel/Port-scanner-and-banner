# Port-scanner-and-banner
Port scanner and banner
Port scanner
Create a function that receives an IP address and a list of port numbers as arguments. The function then
attempts to connect to each port on the list and returns a list of ports that have been confirmed as open by
the function.
Banner grabber
Create a banner-grabbing option. The function receives an IP address, and a confirmed open port number
as arguments and returns the “banner” – I.E the reply message of the port sends back to you after a
successful connection/sent message.
Combine
After creating both functions create a third function that allows you to use the “Port scanner” to find the
open ports of an IP address and then test the banner of each one of the open ports.
a. The function returns the port and banner of each open port.
b. Ports that are open but return no message return “unknown” instead of the banner
c. This will all be formatted as one string:
Example:
IP address – 172.18.0.7
Port 21 open 220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------
… 
