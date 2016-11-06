import socket
import sys

##Use the global broadcast - not because we expect global
# reach , but because it makes the script 0config and we 
# expect it to usded on special purpose networks

UDP_IP = "255.255.255.255"
UDP_PORT = 16725 #('AU' - the 'AtU' message port )


#
# Single threaded assumptions otherwise the backlog will get mixed 
# with new messages.
#


backlog =[]
sock = None
def initialise_subsystem(subsys_name):
    global backlog
    global sock
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

    sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
    try:
	    sock.sendto(subsys_name+" started.", (UDP_IP, UDP_PORT))
    except socket.error, e:
        sock = None 
        return False, e
    else:
        for m in backlog:
            send_msg(m)
        backlog=[]
    return True, None

def send_msg(msg):
    global backlog
    if sock is None:
        backlog.append(msg)
    else:
        sock.sendto(msg, (UDP_IP, UDP_PORT))
