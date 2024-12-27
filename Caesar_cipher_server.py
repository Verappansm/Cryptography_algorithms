import socket

# Caesar cipher for encryption and decryption
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

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  # IP and port
    server_socket.listen(5)
    print("Server started, waiting for connection...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        data = client_socket.recv(1024).decode('utf-8')  # Receive the data
        print(f"Received data: {data}")
        
        # Split data into message and key
        message, key = data.split(",")  # Message and key separated by a comma
        key = int(key)
        
        print(f"Key received: {key}")
        print(f"Encrypted message: {message}")
        
        # Decrypt the message
        decrypted_message = caesar_cipher(message, key, mode="decrypt")
        print(f"Decrypted message: {decrypted_message}")
        
        client_socket.close()

if __name__ == "__main__":
    start_server()
