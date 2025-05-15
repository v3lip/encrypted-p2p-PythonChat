# Encrypted Peer-to-Peer Chat

A simple end-to-end encrypted chat application built in Python using sockets and the `cryptography` library. This tool allows two users to chat securely over a network using symmetric encryption (Fernet).

## 🔐 Features

- Peer-to-peer encrypted messaging
- End-to-end symmetric encryption with Fernet
- Chat history displayed in real time
- Host or connect modes
- Simple and minimal codebase (~100 lines)

## 🛠️ Requirements

- Python 3.x
- `cryptography` library

Install dependencies with:

```bash
pip install cryptography
```

## 🚀 Usage
1. Clone the repository:
```bash
git clone https://github.com/your-username/encrypted-chat.git
cd encrypted-chat
```
2. Run the script:
```bash
python chat.py
```
3. Choose one machine to host the connection (listen), and the other to connect:
### On the host:
```
Hva heter du: Alice
(l)isten eller (c)onnect (l er host, c er kobling mot motpart)? l
```

### On the client:
```
Hva heter du: Bob
(l)isten eller (c)onnect (l er host, c er kobling mot motpart)? c
Skriv inn IPen til motparten: 192.168.x.x
```

Once connected, you can begin chatting securely.

## 🔑 Encryption Key
Note: This project uses a hardcoded symmetric key:
```
key = "ab-YPb_Hzm0_eypRz0bG8bLeReGB1guJvQnYiuCxJoE="
```

In production use, you should:
- Generate a new key using Fernet.generate_key()
- Securely exchange or store the key
- Avoid hardcoding secrets

## ⚠️ Disclaimer
This is a minimal proof-of-concept chat system meant for educational or personal testing. Do not use this in production or expose it to untrusted networks without further security enhancements.

## 📄 License
This project is open-source and available under the MIT License.


# Made with ❤️ in Python
