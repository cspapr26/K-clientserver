import socket
import threading

# Function to send a request to the server
def send_request():
    # Create a socket object using IPv4 and TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the server's host and port
    server_host = 'server-chart.default.svc.cluster.local'
    server_port = 80

    try:
        # Attempt to connect to the server
        client_socket.connect((server_host, server_port))
        print(f"Connected to server {server_host}:{server_port}")

        # Send a request to the server
        client_socket.send("Request".encode())

        # Receive and print the response from the server
        response = client_socket.recv(1024).decode()
        print(f"Response from server: {response}")

    finally:
        # Close the connection when done, regardless of success or failure
        client_socket.close()

# Function to start multiple client threads
def start_clients(num_clients):
    threads = []

    # Create and start specified number of client threads
    for _ in range(num_clients):
        client_thread = threading.Thread(target=send_request)
        threads.append(client_thread)
        client_thread.start()

    # Wait for all threads to finish before moving on
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    # Set the number of parallel clients
    num_clients = 9999999

    # Start the specified number of clients concurrently
    start_clients(num_clients)
