import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SERVER = "192.168.1.198"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def receive():
    while True:
        try:
            msg = client.recv(1024).decode(FORMAT)
            print(msg)
        except:
            print("[ERROR] Connection closed.")
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

print("Enter text to send to the server\nEnter \"disconnect\" to disconnect")

run = True
disconnect = False

while run:
    send_message = input()

    if send_message.lower() == "disconnect":
        send("disconnect")
        disconnect = True
        break
    else:
        send(send_message)
