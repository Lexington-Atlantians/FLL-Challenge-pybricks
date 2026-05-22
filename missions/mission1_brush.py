from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.parameters import Color
from pybricks.tools import wait

WHEEL_DIAMETER_CM = 8.3
WHEEL_CIRCUMFERENCE_CM = WHEEL_DIAMETER_CM * 3.14159

hub = PrimeHub()

motor_left = Motor(Port.A)
motor_right = Motor(Port.E)
arm = Motor(Port.C)

# speed in degrees per second
speed = 450


distance_to_travel_cm = 68.0
num_rotations = distance_to_travel_cm / WHEEL_CIRCUMFERENCE_CM
num_degrees_to_turn = 360.0 * num_rotations

# Convert to msec (speed is in degrees per second)
time_to_turn = num_degrees_to_turn / speed * 1000
print(f"Time to turn: {time_to_turn}")

""" # Move forward
motor_left.run(-speed)
motor_right.run(speed)
print("Moving forward") """

""" wait(time_to_turn)

motor_left.stop()
motor_right.stop() """

wait(500)

#Arm movement (swipe the brushes)
arm.dc(-50)
wait(500)
arm.brake() 

""" # Move backward
motor_left.run(speed)
motor_right.run(-speed)
print("Moving backward")
wait(time_to_turn * 0.4)


motor_left.stop()
motor_right.stop()
 """