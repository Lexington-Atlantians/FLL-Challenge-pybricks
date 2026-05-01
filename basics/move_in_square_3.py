
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.parameters import Color
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub()

motor_left = Motor(Port.A)
motor_right = Motor(Port.E)

turn_speed_at_90_degrees = 180
minimum_speed = 25


def turn_speed_at_n_degrees(n):
    return turn_speed_at_90_degrees * (n / 90.0)


target_heading = -90
tolerance = 0.5
bigger_tolerance = 5.0


while True:
    heading = hub.imu.heading()
    degrees_off = heading - target_heading
    turn_speed = turn_speed_at_n_degrees(degrees_off)

    if abs(turn_speed) < minimum_speed:
        turn_speed = (minimum_speed * (turn_speed / abs(turn_speed)))

    # decide whether to stop
    if abs(degrees_off) < tolerance:
        motor_left.stop()
        motor_right.stop()
        break

    # get the motors going
    motor_left.run(turn_speed)
    motor_right.run(turn_speed)

    # decide whether stalled and if so stop
    average_speed = motor_left.speed(100)
    if abs(average_speed) < .5 and (abs(degrees_off) < bigger_tolerance):
        motor_left.stop()
        motor_right.stop()
        break


wait(200)
print(f"Final heading: {hub.imu.heading()}")


