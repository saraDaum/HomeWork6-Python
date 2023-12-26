"""EX 2.6 client implementation
   Author: Sara Daum
   Date: 18/ 06/2023
"""

import socket
import protocol


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(("127.0.0.1", protocol.PORT))

    while True:
        user_input = input("Please enter command\nAttention: the options are: RAND, NAME, TIME and EXIT\n ")
        # You wrote on page 49 that 'WHORU' is one of the options, I think this is a mistake because the len of
        # 'WHORU' is not 4, and in tha protocol file it's written: (e.g RAND, NAME, TIME, EXIT)
        user_input = user_input.upper()  # To be sure that input is by upper case
        if len(user_input) == 4:
            valid_cmd = protocol.check_cmd(user_input)  # Check user input
            if valid_cmd:  # If the command is valid:
                # 1. Add length field
                msg = protocol.create_msg(user_input)

                # 2. Send it to the server
                my_socket.send(msg.encode())

                # 3. Get server's response
                response_len = my_socket.recv(3).decode()  # length field (between 0-999)
                if response_len.isnumeric():
                    ans = my_socket.recv(int(response_len)).decode()
                else:
                    print("Wrong response")
                    break

                # 4. If server's response is valid, print it
                if ans != 'Wrong command' and ans != 'Wrong protocol' and ans != '' and ans != 'Closing':
                    print(ans)
                if ans == 'Closing':
                    break
            else:
                print("Not a valid command")
        else:
            print("Not a valid command")

    print("Disconnected...\n")
    my_socket.close()


if __name__ == "__main__":
    main()
