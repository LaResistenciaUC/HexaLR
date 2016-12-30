from robot.dynamics import trajectory_calc, ik_angles


prev_angles = None
# Define connection value
ip_num = "192.168.4.1"
port_num = 23
# Calculate trajectory
traj_extension = 50
traj_length = 50
trajectory = list(zip(*trajectory_calc(traj_length, traj_extension, right=True, mod_zyx=(60, 250, 0), debug=True)))
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
        angles = ik_angles(values[2], values[3], values[4])
    else:
        angles = (values[2], values[3], values[4])
    print(angles)

# Confirm
print("Finished!")
