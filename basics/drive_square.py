# Square drive example for Pybricks
# Adjust ports, wheel_diameter and axle_track for your robot.
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait


# Initialize hub and motors
hub = PrimeHub()
left = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
right = Motor(Port.E, positive_direction=Direction.CLOCKWISE)

# Tune these to match your robot (mm)
WHEEL_DIAMETER = 88    # wheel diameter in mm
AXLE_TRACK = 127       # distance between wheels in mm

robot = DriveBase(left, right, WHEEL_DIAMETER, AXLE_TRACK)

# Distance and speed (adjust as needed)
SIDE_LENGTH = 250      # mm per side of the square
DRIVE_SPEED = 200      # mm/s

# Optional: smoother motion
robot.settings(straight_speed=DRIVE_SPEED, straight_acceleration=1000,
               turn_rate=180, turn_acceleration=1000)

# Drive a square: forward SIDE_LENGTH, turn 90 degrees, repeat 4 times
for _ in range(4):
    robot.straight(SIDE_LENGTH)
    robot.turn(90)
    wait(200)

hub.speaker.beep()