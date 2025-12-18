
import socket
import threading
from cryptography.fernet import Fernet

# Generate a key for encryption (In a real scenario, use Diffie-Hellman for key exchange)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_message(message):
    return cipher_suite.encrypt(message.encode())

def decrypt_message(encrypted_message):
    return cipher_suite.decrypt(encrypted_message).decode()

def handle_client(client_socket):
    while True:
        try:
            request = client_socket.recv(1024)
            if not request:
                break
            decrypted_msg = decrypt_message(request)
            print(f"[*] Received encrypted: {request}")
            print(f"[>] Decrypted: {decrypted_msg}")
            
            response = "Message Received secure."
            client_socket.send(encrypt_message(response))
        except Exception as e:
            print(f"[!] Error: {e}")
            break
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print(f"[*] Secure Server listening on port 9999")
    print(f"[*] Encryption Key (Share this securely!): {key.decode()}")
    
    while True:
        client, addr = server.accept()
        print(f"[+] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
