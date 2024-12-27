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

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 65432))

# Input message and key
message = input("Enter the message to encrypt: ")
key = input("Enter the key: ")

# Encrypt the message
encrypted_message = vigenere_cipher(message, key, mode="encrypt")
print(f"Encrypted message: {encrypted_message}")

# Send encrypted message and key
data = f"{encrypted_message},{key}"
client_socket.send(data.encode())

client_socket.close()
