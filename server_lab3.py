import socket

# Vernam cipher
def vernam_cipher(text, key, mode):
    result = []
    for t, k in zip(text, key):
        result.append(chr(ord(t) ^ ord(k)))  # XOR operation
    return ''.join(result)

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 65432))
server_socket.listen(1)
print("Server is waiting for a connection...")

conn, addr = server_socket.accept()
print(f"Connected to client: {addr}")

# Receive data
data = conn.recv(1024).decode()
encrypted_message, key = data.split(',')
print(f"Received encrypted message: {encrypted_message}")
print(f"Received key: {key}")

# Decrypt the message
decrypted_message = vernam_cipher(encrypted_message, key, mode="decrypt")
print(f"Decrypted message: {decrypted_message}")

conn.close()
server_socket.close()
