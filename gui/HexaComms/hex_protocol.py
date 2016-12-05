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
        pack.append(int(alpha))
        pack.append(int(beta))
        pack.append(int(gamma))
        self.sock.send(pack)
