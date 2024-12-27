import socket

# Vernam cipher
def vernam_cipher(text, key, mode):
    result = []
    for t, k in zip(text, key):
        result.append(chr(ord(t) ^ ord(k)))  # XOR operation
    return ''.join(result)

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 65432))

# Input message and key
message = input("Enter the message to encrypt: ")
key = input(f"Enter a key of length {len(message)}: ")

# Ensure the key is the same length as the message
while len(key) != len(message):
    key = input(f"Key must be the same length as the message ({len(message)}): ")

# Encrypt the message
encrypted_message = vernam_cipher(message, key, mode="encrypt")
print(f"Encrypted message: {encrypted_message}")

# Send encrypted message and key
data = f"{encrypted_message},{key}"
client_socket.send(data.encode())

client_socket.close()
