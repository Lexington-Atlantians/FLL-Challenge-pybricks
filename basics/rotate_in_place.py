"""This program makes two motors run in opposite directions.
Hence the robot will rotate 3 seconds clockwise and then 3 seconds counterclockwise.
"""
# TODO : #1 Can we connvert this to a functionthat takes parameters for speed and duration?
# TODO : #2: Can we also make the Ports arguments?
# TODO : #3: Can we develop another function that uses the yaw rate sensor to rotate a specific number of degrees?
# TODO : #4:Can we add this to a library?

from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize a motor on port A.
left_wheel = Motor(Port.A)
right_wheel = Motor(Port.E)

# Make the motors run clockwise at 500 degrees per second.
left_wheel.run(500)
right_wheel.run(500)

# Wait for three seconds.
wait(300)

# Make the motor run counterclockwise at 500 degrees per second.
left_wheel.run(-500)
right_wheel.run(-500)

# Wait for three seconds.
wait(3000)
