import socket

# Vigenère cipher
def vigenere_cipher(text, key, mode):
    key_sequence = (key * ((len(text) // len(key)) + 1))[:len(text)]
    result = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key_sequence[key_index].lower()) - ord('a')
            if mode == "decrypt":
                shift = -shift

            if char.islower():
                result+=(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            else:
                result+=(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            key_index += 1
        else:
            result+=char

    return result

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
decrypted_message = vigenere_cipher(encrypted_message, key, mode="decrypt")
print(f"Decrypted message: {decrypted_message}")

conn.close()
server_socket.close()
