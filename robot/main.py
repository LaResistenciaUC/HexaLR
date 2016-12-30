from dynamics import Controller as ServoController
from dynamics import ik_angles
from dynamics import trajectory_calc

#servos = ServoController()

trayectory = trajectory_calc(15,10,(-5,-15,0),debug=False, samples=20, drop=5)

for point in trayectory:
    print(ik_angles(*point))
