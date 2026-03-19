
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

turn_speed = 180


num_corrections = 1
slow_down_factor = 1.0
tolerance = 50.0
target_value = 90.0

for i in range(num_corrections):
    direction_factor = -1.0
    if i % 2 == 1:
        direction_factor = 1.0

    slow_down_factor = slow_down_factor * 0.5

    tolerance = tolerance * 0.5

    motor_left.run(direction_factor * slow_down_factor * turn_speed)
    motor_right.run(direction_factor * slow_down_factor * turn_speed)

    while True:
        n = hub.imu.heading()
        if abs(n - target_value) < tolerance:
            motor_left.stop()
            motor_right.stop()
            break
        
    wait(200)
    print(f"Heading after turn #{i}: {hub.imu.heading()}")





