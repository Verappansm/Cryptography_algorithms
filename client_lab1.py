import socket

# Caesar cipher for encryption
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            if char.islower():
                result += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            result += char
    return result

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))  # IP and port of the server
    
    message = input("Enter the message to encrypt: ")
    key = int(input("Enter the Caesar cipher key: "))
    
    # Encrypt the message using the Caesar cipher
    encrypted_message = caesar_cipher(message, key, mode="encrypt")
    print(f"Encrypted message: {encrypted_message}")
    
    # Send the encrypted message and key to the server
    data_to_send = f"{encrypted_message},{key}"
    client_socket.send(data_to_send.encode('utf-8'))  # Send data to the server
    
    client_socket.close()

if __name__ == "__main__":
    start_client()
