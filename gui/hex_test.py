from math import acos, atan, sqrt, pi

PI = pi
COXA = 30
FEMUR = 92
TIBIA = 169


def sq(val):
    return val * val


def constrain(val, mini, maxi):
    if val < mini:
        return mini
    elif val > maxi:
        return maxi
    return val


def opti(val):
    if 180 < val <= 360:
        return 360 - val
    return val


def ik(x, y, z):
    l1 = sqrt(sq(x) + sq(y))
    l = sqrt(sq(l1 - COXA) + sq(z))
    alpha1 = acos(z / l) / PI * 180
    try:
        alpha2 = acos((sq(FEMUR) + sq(l) - sq(TIBIA)) / (2 * FEMUR * l)) / PI * 180
    except ValueError:
        i = (sq(FEMUR) + sq(l) - sq(TIBIA)) / (2 * FEMUR * l)
        alpha2 = acos(constrain(i, -1, 1)) / PI * 180
    theta1 = int(alpha1 + alpha2)
    try:
        theta2 = int(acos((sq(TIBIA) + sq(FEMUR) - sq(l)) / (2 * TIBIA * FEMUR)) / PI * 180)
    except ValueError:
        j = (sq(TIBIA) + sq(FEMUR) - sq(l)) / (2 * TIBIA * FEMUR)
        theta2 = int(acos(constrain(j, -1, 1)) / PI * 180)
    theta3 = int(atan(x / y) / PI * 180)
    return opti(theta1), opti(theta2), opti(theta3)

while True:
    _x = int(input("x "))
    _y = int(input("y "))
    _z = int(input("z "))

    print(ik(_x, _y, _z))