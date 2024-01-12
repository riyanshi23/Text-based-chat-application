# Import required modules
import socket
import threading

# Function to handle client connections
def handle_client(client_socket, addr):
    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break # If no data, break the loop

            print(f"Received from {addr}: {data}")

            # Send a response to the client
            response = input("Server: ") # Get input from the server
            client_socket.send(response.encode('utf-8'))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the connection when done
        client_socket.close()

# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5555))
server.listen(5)

print("Server listening on port 5555")

# Main loop to accept client connections
while True:
    client_sock, client_addr = server.accept()
    print(f"Accepted connection from {client_addr}")

    # Create a new thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client_sock, client_addr))
    client_handler.start()