Implement sending "Hello World" from client to server via UDP using Twisted Lib. (Links to an external site.)Links to an external site.

https://twisted.readthedocs.io/en/twisted-17.9.0/index.html (Links to an external site.)Links to an external site.

 

Submission:

 

1.  URL to your Lab 3 Github Repo. Your repo should have the following files:

connected_udp_client.py
connected_udp_server.py
multicast_udp_client.py
multicast_udp_server.py
2. Answer to this question: "What happened when you send message from client in Multicast UDP when server is not available?"
	The clients were able to communicate to each other without the server, because in Multicast there is no server/client differentiation at the protocol level.