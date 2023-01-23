import socket
import threading


HEADER = 64
PORT = 5050
# SERVER = "IP_ADDRESS"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handleClient(conn , addr):
    print(f"[NEW CONNECTION] {addr} connected")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #blocking line of code
        if msg_length:
            msg_length = int(msg_length)
            msg =conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            print(f"[{addr}] {msg}")
            conn.send("msg reseved".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print("[LISTENING] server is listening on {SERVER}")

    while True:
        conn , addr = server.accept()
        thread = threading.Thread(target=handleClient,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}") # - start cuz always running


print("[STARTING] server is starting... ")
start()
