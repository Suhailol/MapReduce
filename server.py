import socket

HOST = socket.gethostname()
PORT  = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print("connected by addr")
        while True:
            data = conn.recv(1024)
            if data:
                print("Client: ", data.decode())
            data  = input("Enter a message to client")
            if not data:
                break
            conn.send(data.encode(ascii))
        conn.close()

