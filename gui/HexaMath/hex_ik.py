import math


COXA_LENGTH = 30
FEMUR_LENGTH = 92
TIBIA_LENGTH = 169


def ik_angles2(x, y, z, l1, l2, l3,inv3=1,inv2=1):
    q1 = math.atan(y/x)
    cosq3 = (x**2+y**2+z**2-l2**2-l3**2) / (2*l2*l3)
    q3 = math.atan2(inv3*math.sqrt(1-cosq3**2),cosq3)
    q2 = math.atan2(z,inv2*math.sqrt(x**2+y**2))-math.atan2(l3*math.sin(q3),l2+l3*math.cos(q3))
    return q1, q2, q3


def ik_angles(ik_feet_pos_x, ik_feet_pos_y, ik_feet_pos_z, leg_ik_leg_nr):

    is_right_side = (leg_ik_leg_nr == 2) or (leg_ik_leg_nr == 4) or (leg_ik_leg_nr == 6)

    # iksw                      = 0  # Length between Femur and Tibia
    # ikradiansfemurtibiaground = 0  # Angle of the line Femur and Tibia with respect to the ground in radians
    # ikradiansfemurtibia       = 0  # Angle of the line Femur and Tibia with respect to the femur in radians
    # ikfeetposxz               = 0  # Distance between the Coxa and Ground Contact

    ikfeetposxz = math.sqrt(math.pow(ik_feet_pos_x, 2) + math.pow(ik_feet_pos_z, 2))

    iksw = math.sqrt(math.pow((ikfeetposxz - COXA_LENGTH), 2) + math.pow(ik_feet_pos_y, 2))

    ikradiansfemurtibiaground = math.atan2(ikfeetposxz - COXA_LENGTH, ik_feet_pos_y)

    ikradiansfemurtibia = math.acos(((math.pow(FEMUR_LENGTH, 2) - math.pow(TIBIA_LENGTH, 2)) + math.pow(iksw, 2)) / (2 * FEMUR_LENGTH * iksw))

    coxa_angle = math.atan2(ik_feet_pos_z, ik_feet_pos_x) * 180 / math.pi

    femur_angle = -(ikradiansfemurtibiaground + ikradiansfemurtibia) * 180 / math.pi + 90

    tibia_angle = -(90 - (((math.acos((math.pow(FEMUR_LENGTH, 2) + math.pow(TIBIA_LENGTH, 2) - math.pow(iksw, 2)) /
                                      (2 * FEMUR_LENGTH * TIBIA_LENGTH))) * 180) / math.pi))

    if not is_right_side:

        femur_angle = abs(femur_angle)
        tibia_angle = abs(tibia_angle)
    # return coxa_angle, femur_angle, tibia_angle
    return femur_angle, coxa_angle, tibia_angle

if __name__ == '__main__':
    # Test Ouput
    print(ik_angles(86, 20, 150, 2))
    # print(ik_angles(86, 106, 0, 1))
    # print(ik_angles(86, 106, 0, 2))
    # print(ik_angles(86, 106, 0, 3))
    # print(ik_angles(86, 106, 0, 4))
    # print(ik_angles(86, 106, 0, 5))
