import socket
import os  # For printing the full path

if __name__ == '__main__':
    # Defining Socket
    host = '127.0.0.1'
    port = 8080
    total_client = int(input('Enter number of clients: '))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(total_client)

    # Establishing Connections
    connections = []
    print('Server is listening for client connections...')
    for i in range(total_client):
        conn, addr = sock.accept()  # Accept a connection
        connections.append(conn)
        print(f'Connected with client {i + 1} at {addr}')

    fileno = 0
    idx = 0
    for conn in connections:
        # Receiving File Data
        idx += 1
        filename = 'output' + str(fileno) + '.txt'
        fileno += 1
        file_path = os.path.abspath(filename)  # Get the absolute file path
        print(f'File will be saved at: {file_path}')  # Debugging line

        with open(filename, "wb") as fo:
            while True:
                data = conn.recv(1024)  # Receiving data in chunks of 1024 bytes
                if not data:
                    print("No more data received. Ending file transfer.")
                    break
                print(f'Received data chunk: {data[:20]}...')  # Debugging: print first 20 bytes of data received
                fo.write(data)  # Write received data to file

        print(f'File received successfully! New filename is: {filename}')
        conn.close()

    # Closing the server socket
    sock.close()
    print('Server has closed the connection.')
