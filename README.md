GhoulLazer developed by Hari Patel (hari.p.221221@gmail.com) (github.com/Hari-P-22121)

GhoulLazer is a Denial Of Service tool for stress testing. 

GhoulLazer floods systems through ping flooding. GhoulLazer is able to go past the limit without requiring root privileges allowed by having multiple threads. This means that GhoulLazer will have multiple ping sessions open. The number of sessions is known as threads which the user can enter and choose. There is no limit. The user must enter a number.

When the software starts, the client will have to enter an IP/Hostname that will be stress tested. Then they must enter how many to send per thread (MAX: 8000 bytes PER THREAD). Which means they can have multiple threads and send more bytes per second to the system faster (They will be prompted on how many threads to run). After this, they are required to enter how many times to send ping the host. (NOTE: The total of bytes being sent can be calculated by multiplying the 3 values above.) Then there is the delay between each shot. The shorter the delay, the faster the bytes will be sent and the more effective. However if the delay is too short, then majority of the bytes will time out and/or the victim will ignore most.  
