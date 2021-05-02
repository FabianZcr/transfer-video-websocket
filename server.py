from socket import socket, gethostname
from moviepy.editor import *

# Function to convert video to any other video format
def convert_video(video_file, video_format):
    print('SERVER> Converting video...')
    new_format = "video_new_"+ str((n-1)) + video_format
    videoClip = VideoFileClip(video_file).write_videofile(new_format)
    print('SERVER> Converting done')

# Server configuration
s = socket()
host = gethostname()
port = 3399

# Server params
server_address = (host, port)
max_conecctions = 10
print('SERVER> Starting up on {} port {}'.format(*server_address))
s.bind(server_address)
s.listen(max_conecctions) 
n = 0

while True:
    print('\nSERVER> Waiting for a connection')
    connection, addr = s.accept()

    try:
        print('SERVER> Connection from', addr)
        print("SERVER> Starting to read bytes..")
        buffer = connection.recv(1024)
    
        with open('video_'+str(n)+'.mp4', "wb") as video:
            n += 1
            i = 0
            while buffer:                
                video.write(buffer)
                i += 1
                buffer = connection.recv(1024)
        print("SERVER> Done reading bytes..")

        # Convert video to new format
        convert_video('video_'+str(n-1)+'.mp4', ".webm")

    except KeyboardInterrupt:
        if connection:
            print("SERVER> Disconecting client")
            connection.close()
        break

s.close()
print("SERVER> Connection closed")