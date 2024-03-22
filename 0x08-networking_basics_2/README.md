localhost: a special address for loopbacking; sending to the same local device for testing purposes 127.0.0.1

0000: for undefined IP when not getting an IP from DHCP (acts like a placeholder), it also used for socket listening in local networking to allow the socket to accept connection from any IP address in the system; as an application for that last one, is BLUETOOTH set the socket in your device to 0.0.0.0 to accept connection from other devices in the same area

what is the DNS?
DNS stands for Domain Name System. It's a hierarchical decentralized naming system for computers, services, or any resource connected to the internet or a private network. DNS translates domain names (e.g., www.example.com) into IP addresses (e.g., 192.0.2.1), which computers use to identify each other on the network.

Here's how DNS works:

Domain Names: Domain names are human-readable labels used to identify resources on the internet. They consist of a sequence of characters separated by dots (e.g., www.example.com).

DNS Resolver: When you enter a domain name into a web browser or other network application, your device's DNS resolver (usually provided by your Internet Service Provider or configured manually) performs a DNS query to find the corresponding IP address.

DNS Query: The DNS resolver sends a DNS query to a DNS server, requesting the IP address associated with the domain name.

