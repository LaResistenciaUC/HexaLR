from time import sleep

from gui.HexaComms import HexConnector

# Define connection value
ip_num = "192.168.4.1"
port_num = 23
# Calculate trajectory
traj_extension = 150
traj_length = 150
trajectory = list(zip(*trajectory_calc(traj_length, traj_extension, right=True, mod_xyz=(40, 100, 0), debug=True)))
# trajectory = {"{}".format(n): 70 for n in range(1, 19)}
# Establish connection
comms = HexConnector(ip_num, port_num, payload_len=18)
print("Connected to {} on port {}.".format(ip_num, port_num))
# Send out data
# for point in trajectory:
#     # print(point)
#     # Calculate angles from XYZ point
#     angles = ik_angles(*point, leg_ik_leg_nr=True)
#     print(angles)
#     # Send data over
#     comms.test_comms(*angles)
#     # Sleep before sending more data
#     sleep(0.200)
for _ in range(5):
    comms.dict_angle_comms(trajectory)
    trajectory = {"{}".format(n): 90 for n in range(1, 19)}
    sleep(1.000)
# Confirm
print("Finished!")
# input("Press enter to delete plot!")
