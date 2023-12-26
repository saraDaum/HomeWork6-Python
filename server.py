"""EX 2.6 server implementation
   Author: Sara Daum
   Date:
"""
from datetime import datetime
import random
import socket
import protocol


def create_server_rsp(cmd):
    """Based on the command, create a proper response"""
    if cmd == 'RAND':
        return str(random.randint(1, 10))
    if cmd == 'NAME':
        return "Sara's servers"
    if cmd == 'EXIT':
        return "Closing"
    if cmd == 'TIME':
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time
    return "Server response"


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", protocol.PORT))
    server_socket.listen()
    print("Server is up and running")

    (client_socket, client_address) = server_socket.accept()
    print("Client connected")

    while True:
        # Get message from socket and check if it is according to protocol

        valid_msg, cmd = protocol.get_msg(client_socket)
        if valid_msg:
            # 1. Print received message
            print("Received message: " + cmd)

            # 2. Check if the command is valid
            valid_cmd = protocol.check_cmd(cmd)

            # 3. If valid command - create response
            if valid_cmd:
                response = create_server_rsp(cmd)

        if valid_cmd == False:
            print("Invalid command.")
            response = "Wrong command"
            client_socket.recv(1024)  # Attempt to empty the socket from possible garbage

        # Send response to the client
        response = protocol.create_msg(response)
        client_socket.send(response.encode())
        if cmd == "EXIT":
            break

    #  In the end - close all sockets
    client_socket.close()
    server_socket.close()
    print("Server disconnected...")


if __name__ == "__main__":
    main()


