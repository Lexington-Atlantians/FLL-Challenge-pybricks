from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.parameters import Direction
from pybricks.parameters import Color
from pybricks.tools import wait


DUTY_CYCLE = 50

hub = PrimeHub()

motor_left = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.E)


initial_yaw = hub.imu.heading()


motor_left.dc(DUTY_CYCLE + 1.5)
motor_right.dc(DUTY_CYCLE)


wait(7000)

motor_left.brake()
motor_right.brake()

final_yaw = hub.imu.heading()


print(f"final yaw = {final_yaw} OH YEAH ")