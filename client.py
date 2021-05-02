from socket import socket, gethostname, SHUT_WR
import time

def get_video():
    print("CLIENT> Downloading video..")
    time.sleep(20)
    print("CLIENT> Download succesfull")

s = socket()
host = gethostname()
port = 3399

# Connect the socket to the port where the server is listening
server_address = (host, port)
print('CLIENT> Connecting to {} port {}'.format(*server_address))
s.connect(server_address)
print("CLIENT> Sending video...")

with open("./clientVideos/test.mp4", "rb") as video:
    buffer = video.read()
    s.sendall(buffer)

print("CLIENT> Done sending")
s.close()

get_video()
print("CLIENT> Conecction closed")