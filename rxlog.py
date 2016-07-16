import socket, datetime

UDP_IP = "0.0.0.0"
UDP_PORT = 16725 #('AU' - the 'AtU' message port )

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print datetime.datetime.now().strftime("%c")," - ", data
