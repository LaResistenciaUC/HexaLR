from socket import socket, AF_INET, SOCK_STREAM


# Generates packet to send to robot over sockets
def packet_generator(xyz_dict):
    packet = bytearray()
    for coord in sorted(xyz_dict.items(), key=lambda x: x[0]):
        for val in coord[1]:
            packet.append(val)
    return packet

IP = "192.168.4.1"
PORT = 23
payload_debug = True
# TODO Implement handshake from ESP
connected = False

coord_dict = {'5': [13, 14, 15], '3': [7, 8, 9],
              '6': [16, 17, 40], '4': [10, 11, 12],
              '2': [4, 5, 6], '1': [1, 2, 3]}

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((IP, PORT))
print("Opened socket")

payload = packet_generator(coord_dict)
if payload_debug:
    print(list(payload))
sock.send(payload)
print("Done!")
