from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.parameters import Color
from pybricks.tools import wait


def print_yaw(hub):
    heading = hub.imu.heading()
    print(f"Current yaw is {heading}")



# Initialize the hub.
hub = PrimeHub()

motor_left = Motor(Port.A)
motor_right = Motor(Port.E)

speed = 100
duration = 1000

print_yaw(hub)

motor_left.run(-speed)
motor_right.run(speed)
wait(duration)

motor_left.stop()
motor_right.stop()

wait(1000)
print_yaw(hub)