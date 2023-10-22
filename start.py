import socket
import threading
from cryptography.fernet import Fernet
import json
import sys, os
import threading

key = "ab-YPb_Hzm0_eypRz0bG8bLeReGB1guJvQnYiuCxJoE="
cipher = Fernet(key)
print(f"Nøkkel: {key}")


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

chat_history = [] 

def send_message(sock):
    while True:
        msg = input()
        chat_history.append(f"{username}: {msg}")
        clear_console()
        for line in chat_history:
            print(line)
        
        data_obj = {
            "username": username,
            "message": msg
        }
        encrypted_msg = cipher.encrypt(json.dumps(data_obj).encode())
        sock.sendall(encrypted_msg)

def receive_message(sock):
    while True:
        data = sock.recv(1024)
        decrypted_msg = cipher.decrypt(data).decode()
        msg_obj = json.loads(decrypted_msg)
        chat_history.append(f"{msg_obj['username']}: {msg_obj['message']}")
        
        clear_console()
        for line in chat_history:
            print(line)


def main():
    global username
    username = input("Hva heter du fitte: ")

    choice = input("(l)isten eller (c)onnect (l er host, c er kobling mot motpart)? ")

    if choice == 'l':
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', 12345))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by: {addr}")
                threading.Thread(target=receive_message, args=(conn,), daemon=True).start()
                send_message(conn)
    elif choice == 'c':
        host = input("Skriv inn IPen til fitten i andre enden: ")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, 12345))
            threading.Thread(target=receive_message, args=(s,), daemon=True).start()
            send_message(s)

if __name__ == "__main__":
    main()