import socket
import threading

# Set up the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

# Function to send and receive messages
def send_receive():
    try:
        while True:
            # Send a message to the server
            message = input("Client: ")
            client.send(message.encode('utf-8'))

            # Receive response from the server
            response = client.recv(1024).decode('utf-8')
            print(f"Received from server: {response}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the connection when done
        client.close()

# Run the send_receive function in a separate thread
send_receive_thread = threading.Thread(target=send_receive)
send_receive_thread.start()
