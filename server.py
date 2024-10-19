import socket
import threading

HEADER = 64
PORT = 5050
SERVER = "192.168.1.198"
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "disconnect"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

clients = []


def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(conn, addr):

    clients.append(conn)
    print(f"[NEW CONNECTION]: {addr} Connected" )
    connected = True

    try:
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if not msg_length:
                    break
            
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg.lower() == DISCONNECT_MESSAGE:
                connected = False
                conn.send("Disconected From Server!".encode(FORMAT))
                print(f"[CONNECTION CLOSED] {addr} Disconnected From Server")
                clients.remove(conn)
                conn.close()
                broadcast(f"[{addr}]: disconnected".encode(FORMAT), conn)

            else:    
                print(f"[{addr}]: {msg}")
                broadcast(f"[{addr}]: {msg}".encode(FORMAT), conn)
            
    except ConnectionResetError as e:
        print(f"[ERROR] Connection reset by {addr}: {e}")
    
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")

def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]: {threading.active_count()-1}")

print("[STARTING] server is starting...")
start()
