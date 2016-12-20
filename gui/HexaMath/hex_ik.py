from math import atan2, sqrt, pow, pi, acos, sin, cos, degrees


COXA_LENGTH = 30
FEMUR_LENGTH = 92
TIBIA_LENGTH = 169


def ik_angles3(x,y,z,l1=COXA_LENGTH,l2=FEMUR_LENGTH,l3=TIBIA_LENGTH):
    ##l1=distancia entre el origen y el 1° actuador
    ##l2= entre el 1° y el 2°
    ##l3= entre el 2° y el 3°
    ##estos calculos estan hechos pensando que el eje z esta invertido
    q1 = atan2(y, x)
    cosq3 = (x ** 2 + y ** 2 + (z - l1) ** 2 - l2 ** 2 - l3 ** 2) / (2 * l2 * l3)
    q3 = atan2(-sqrt(1 - cosq3 ** 2), cosq3)
    q2 = atan2(z - l1, sqrt(x ** 2 + y ** 2)) - atan2(-l3 * sqrt(1 - cosq3 ** 2), l2 + l3 * cosq3)
    return degrees(q1), degrees(q2), degrees(q3)


def ik_angles2(x, y, z, l1, l2, l3,inv3=1,inv2=1):
    q1 = atan2(y,x)
    cosq3 = (x**2+y**2+z**2-l2**2-l3**2) / (2*l2*l3)
    q3 = atan2(inv3*sqrt(1-cosq3**2),cosq3)
    q2 = atan2(z,inv2*sqrt(x**2+y**2))-atan2(l3*sin(q3),l2+l3*cos(q3))
    return degrees(q1), degrees(q2), degrees(q3)


def ik_angles(ik_feet_pos_x, ik_feet_pos_y, ik_feet_pos_z, leg_ik_leg_nr):

    is_right_side = (leg_ik_leg_nr == 2) or (leg_ik_leg_nr == 4) or (leg_ik_leg_nr == 6)

    # iksw                      = 0  # Length between Femur and Tibia
    # ikradiansfemurtibiaground = 0  # Angle of the line Femur and Tibia with respect to the ground in radians
    # ikradiansfemurtibia       = 0  # Angle of the line Femur and Tibia with respect to the femur in radians
    # ikfeetposxz               = 0  # Distance between the Coxa and Ground Contact

    ikfeetposxz = sqrt(pow(ik_feet_pos_x, 2) + pow(ik_feet_pos_z, 2))

    iksw = sqrt(pow(    (ikfeetposxz - COXA_LENGTH), 2) + pow(ik_feet_pos_y, 2))

    ikradiansfemurtibiaground = atan2(ikfeetposxz - COXA_LENGTH, ik_feet_pos_y)

    ikradiansfemurtibia = acos(((pow(FEMUR_LENGTH, 2) - pow(TIBIA_LENGTH, 2)) + pow(iksw, 2)) / (2 * FEMUR_LENGTH * iksw))

    coxa_angle = atan2(ik_feet_pos_z, ik_feet_pos_x) * 180 / pi

    femur_angle = -(ikradiansfemurtibiaground + ikradiansfemurtibia) * 180 / pi + 90

    tibia_angle = -(90 - (((acos((pow(FEMUR_LENGTH, 2) + pow(TIBIA_LENGTH, 2) - pow(iksw, 2)) /
                                      (2 * FEMUR_LENGTH * TIBIA_LENGTH))) * 180) / pi))

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
