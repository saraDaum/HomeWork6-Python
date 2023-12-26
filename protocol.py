"""EX 2.6 protocol implementation
   Author: Sara Daum
   Date: 18/06/2023
"""

LENGTH_FIELD_SIZE = 3
PORT = 8820


def check_cmd(data):
    """Check if the command is defined in the protocol (e.g RAND, NAME, TIME, EXIT)"""
    if data == 'RAND' or data == 'NAME' or data == 'TIME' or data == 'EXIT':
        return True
    return False


def create_msg(data):
    """Create a valid protocol message, with length field"""
    length = str(len(data))
    zfill_length = length.zfill(LENGTH_FIELD_SIZE)  # make sure
    return zfill_length + data


def get_msg(my_socket):
    """Extract message from protocol, without the length field
       If length field does not include a number, returns False, "Error" """
    socket_len = my_socket.recv(LENGTH_FIELD_SIZE).decode()  # length field (between 0-999)
    if socket_len.isnumeric():
        return True, my_socket.recv(int(socket_len)).decode()
    return False, "Error"


