from math import sin, cos, asin, acos, atan2, pi

COXA_LENGTH = 30
FEMUR_LENGTH = 92
TIBIA_LENGTH = 169


def ik_angles(x, y, z, l0=COXA_LENGTH, l1=FEMUR_LENGTH, l2=TIBIA_LENGTH):
    q1 = atan2(x, y)
    d = ((x - l0 * cos(q1))**2 + (y - l0 * sin(q1))**2 + z**2)**(1/2)
    b = acos((d**2 + l1**2 - l2**2)/(2*l1*d))
    q2 = asin((-z)/d) - b
    cos_1 = acos((l1*sin(b))/l2)
    cos_2 = pi/2 - b
    q3 = pi - cos_1 - cos_2
    return q1, q2, q3
