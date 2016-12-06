from socket import socket, AF_INET, SOCK_STREAM
import binascii


class ChecksumException(Exception):
    pass


class PacketLengthException(Exception):
    pass


class HexConnector:

    def __init__(self, ip, port, payload_len=40):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((ip, port))
        self.payload_len = payload_len

    # Generates packet to send to robot over sockets. Then, proceeds to obtain an answers, stores the
    # values in dictionaries, verifies them and returns them
    # TODO Sanitize dictionary values
    def send_message(self, config_dict, state_dict):
        # Empty packet message
        packet = bytearray()
        # BYTE 0 - 2: Packet number from config in LSB
        packet.extend((config_dict['packet_no']).to_bytes(3, byteorder='little'))
        # BYTE 3: Robot state
        packet.extend(bytearray(config_dict['robot_state'], 'ascii'))
        # BYTE 4, 5: Round trip (ms) in LSB
        packet.extend((config_dict['round_trip']).to_bytes(2, byteorder='little'))
        # BYTE 6, 7: Missed packets in LSB
        packet.extend((config_dict['missed_packets']).to_bytes(2, byteorder='little'))
        # BYTE 8: IK - DK selector
        packet.extend(bytearray(config_dict['ik_dk'], 'ascii'))
        # BYTE 9, 10: Padding
        packet.extend((config_dict['padding']).to_bytes(2, byteorder='little'))
        # BYTE 11 - 28: XYZ coordinates / ABC angles (depending on ik_dk)
        for coord in sorted(state_dict.items(), key=lambda x: x[0]):
            for val in coord[1]:
                packet.append(val)
        # BYTE 29 - 35: Future use bytes. Padding
        packet.extend((config_dict['padding']).to_bytes(7, byteorder='little'))
        # BYTE 36: Padding
        packet.extend((config_dict['padding']).to_bytes(1, byteorder='little'))
        # Checksum calculation. Append 4 bytes of padding for calculation, compute CRC32
        # and replace last 4 empty bytes with checksum
        packet.extend((config_dict['padding']).to_bytes(4, byteorder='little'))
        crc = binascii.crc32(packet)
        packet = packet[:-4]
        packet.extend(crc.to_bytes(4, byteorder='little'))
        # Verify packet length and return packet
        if len(packet) != self.payload_len:
            raise PacketLengthException("Packet length is {}!".format(len(packet)))
        # Send packet
        self.sock.send(packet)
        # Obtain answer, process and insert into dictionaries and verify them
        data_in = list(bytearray(self.sock.recv(self.payload_len)))
        t_config_dict, t_state_dict = {}, {}
        t_config_dict['packet_no'] = data_in[0] + (data_in[1] << 8) + (data_in[2] << 16)

    def dict_angle_comms(self, state_dict):
        packet = bytearray()
        # BYTE 0 - 17: XYZ coordinates / ABC angles (depending on ik_dk)
        for coord in sorted(state_dict.items(), key=lambda x: int(x[0])):
            packet.append(int(coord[1]))
        # Verify packet length and return packet
        if len(packet) != self.payload_len:
            raise PacketLengthException("Packet length is {}!".format(len(packet)))
        # Send packet
        self.sock.send(packet)

    def test_comms(self, alpha, beta, gamma):
        pack = bytearray()
        fx = lambda x: int(-0.711*(-x - 180))
        pack.append(fx(alpha))
        pack.append(fx(beta))
        pack.append(fx(gamma))
        self.sock.send(pack)

    def full_comms(self, a1=90,b1=90,g1=90, a2=90,b2=90,g2=90, a3=90,b3=90,g3=90, a4=90,b4=90,g4=90, a5=90,b5=90,g5=90, a6=90,b6=90,g6=90):
        pack = bytearray()
        fx = lambda x: int(-0.711*(-x - 180))
        pack.append(fx(a1))
        pack.append(fx(b1))
        pack.append(fx(g1))

        pack.append(fx(a2))
        pack.append(fx(b2))
        pack.append(fx(g2))

        pack.append(fx(a3))
        pack.append(fx(b3))
        pack.append(fx(g3))

        pack.append(fx(a4))
        pack.append(fx(b4))
        pack.append(fx(g4))

        pack.append(fx(a5))
        pack.append(fx(b5))
        pack.append(fx(g5))

        pack.append(fx(a6))
        pack.append(fx(b6))
        pack.append(fx(g6))

        self.sock.send(pack)
