import socket

##Use the global broadcast - not because we expect global
# reach , but because it makes the script 0config and we 
# expect it to usded on special purpose networks

UDP_IP = "255.255.255.255"
UDP_PORT = 16725 #('AU' - the 'AtU' message port )
MESSAGE = "Hello, World!"


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))











