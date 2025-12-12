# NetworkExperiment
about computer network experiment at school

Experiment Requirement:

1. Write a Python program that uses TCP socket to connect to a HTTP server (e.g. http://gaia.cs.umass.edu), ask for a HTML page (e.g. /wireshark-labs/HTTP-wireshark-file1.html)
2. Write a Python program that waits for a connection on a TCP port, and be able to receive and interpret HTTP requests, and sends a HTTP Response answering the request. Here, we may use the HTTP Response, which includes a basic HTML file (<HTML> Hello world </HTML>). The server handles only one single client at a time.
> Improve the response of the server by including other information in the Header, such as current time, name of the machine running the server, its OS, Python version as well as information on the client such as: IP address, Web browser version, etc.
3. Write a HTTP server capable of sending files included in the Requests. To do that, create a directory where you host the web files. If the file requested by a client does not exist, the server should response by an appropriate HTTP Response code.
