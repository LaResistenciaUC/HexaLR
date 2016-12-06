from time import sleep

from gui.HexaComms import HexConnector
from gui.HexaMath import trajectory_calc, ik_angles3


prev_angles = None
# Define connection value
ip_num = "192.168.4.1"
port_num = 23
# Calculate trajectory
traj_extension = 50
traj_length = 50
trajectory = list(zip(*trajectory_calc(traj_length, traj_extension, right=True, mod_zyx=(60, 250, 0), debug=True)))
# Establish connection
comms = HexConnector(ip_num, port_num, payload_len=18)
print("Connected to {} on port {}.".format(ip_num, port_num))
# Send out data
# for point in trajectory:
#     print(point)
#     # Calculate angles from XYZ point
#     try:
#         angles = ik_angles3(*point)
#     except:
#         angles = prev_angles
#     print(angles)
#     # Send data over
#     comms.test_comms(*angles)
#     # Sleep before sending more data
#     prev_angles = angles
#     sleep(0.200)
# Confirm
# print("Finished!")

while True:
    input_val = input("Leg[1-6], UseIK[0/1], X/alpha, Y/beta, Z/gamma: ")
    values = input_val.split(",")
    if len(values) != 5:
        break
    if values[1]:
        angles = ik_angles3(values[2],values[3], values[4])
    else:
        angles = (values[2],values[3], values[4])
    print(angles)
    if values[0] == 1:
        comms.full_comms(a1=angles[0],b1=angles[1],g1=angles[2])
    elif values[0] == 2:
        comms.full_comms(a2=angles[0],b2=angles[1],g2=angles[2])
    elif values[0] == 3:
        comms.full_comms(a3=angles[0],b3=angles[1],g3=angles[2])
    elif values[0] == 4:
        comms.full_comms(a4=angles[0],b4=angles[1],g4=angles[2])
    elif values[0] == 5:
        comms.full_comms(a5=angles[0],b5=angles[1],g5=angles[2])
    elif values[0] == 6:
        comms.full_comms(a6=angles[0],b6=angles[1],g6=angles[2])
# Confirm
print("Finished!")
