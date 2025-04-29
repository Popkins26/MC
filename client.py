import socket

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        print("Attempting to connect to server...")
        sock.connect((host, port))  # This will block until the server is ready to accept the connection
        print("Client connected to server.")
        
        while True:
            filename = input('Input filename you want to send (or type "exit" to quit): ')
            
            # Exit condition for the client
            if filename.lower() == "exit":
                print("Exiting client...")
                break  # Exit the loop if the user types 'exit'

            print(f"File to send: {filename}")  # Debugging line

            try:
                with open(filename, "rb") as fi:
                    print(f'Reading and sending file: {filename}...')
                    data = fi.read(1024)
                    while data:
                        print(f'Sending data chunk: {data[:20]}...')  # Debugging: print first 20 bytes of data
                        sock.send(data)  # Send the chunk of data
                        data = fi.read(1024)  # Read the next chunk
                    print(f'File {filename} sent successfully.')

                # Optionally, you can send an EOF signal (e.g., a specific byte) after the file is sent, if needed.
                # sock.send(b'EOF')  # Unnecessary if server just closes after receiving no data

            except IOError:
                print('You entered an invalid filename! Please enter a valid name.')

    except Exception as e:
        print(f"Error connecting to server: {e}")
    finally:
        sock.close()
