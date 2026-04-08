from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.parameters import Color
from pybricks.tools import wait

hub = PrimeHub()

motor_left = Motor(Port.A)
motor_right = Motor(Port.E)

speed = 450

#wheel_circumference_cm = 8.3 * 3.14159
#distance_to_travel = 45.3
#num_rotations = distance_to_travel / wheel_circumference_cm
#num_degrees_to_turn = 360.0 * num_rotations

#time_to_turn = num_degrees_to_turn / speed
time_to_turn = 1.389
#print(f"Time to turn: {time_to_turn}")

# Move forward
motor_left.run(-1 * speed)
motor_right.run(speed)

wait(time_to_turn)

motor_left.stop()
motor_right.stop()

# Code to solve Mission 1