import socket
import time
import threading
import platform

# Function to handle a client connection
def handle_client(client_socket):
    # Simulate processing time (e.g., data processing, computation)
    time.sleep(5)

    # Get the hostname of the server
    server_hostname = platform.node()

    # Send the hostname back to the client
    client_socket.send(server_hostname.encode())

    # Close the connection after processing
    client_socket.close()

# Function to start the server
def start_server():
    # Create a socket object using IPv4 and TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set the server's host and port
    server_host = '0.0.0.0'
    server_port = 8080

    # Bind the socket to the specified host and port
    server_socket.bind((server_host, server_port))
    
    # Listen for incoming connections, allow up to 5 queued connections
    server_socket.listen(5)
    print(f"Server listening on {server_host}:{server_port}")

    while True:
        # Accept a connection when it arrives
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        # Handle each connection in a separate thread
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    # Start the server
    start_server()
