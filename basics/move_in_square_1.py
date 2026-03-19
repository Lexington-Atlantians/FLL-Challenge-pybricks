
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.parameters import Color
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub()

motor_left = Motor(Port.A)
motor_right = Motor(Port.E)

forward_duration = 1000
forward_speed = 180

turn_duration = 900
turn_speed = 180

for i in range(4):

    motor_left.run(-forward_speed)
    motor_right.run(forward_speed)
    wait(forward_duration)

    motor_left.stop()
    motor_right.stop()

    motor_left.run(turn_speed)
    motor_right.run(turn_speed)

    wait(turn_duration)





