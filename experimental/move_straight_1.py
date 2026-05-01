
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.parameters import Direction
from pybricks.parameters import Color
from pybricks.tools import wait
from pybricks.tools import StopWatch


# Initialize the hub.
hub = PrimeHub()

motor_left = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.E)

LOOP_INTERVAL_MS   = 20   # how often to update the loop (ms)


def move_straight_naive():
    readings = [None, None]
    readings[0] = hub.imu.heading()
    motor_left.dc(50)
    motor_right.dc(50)
    wait(3500)
    motor_left.brake()
    motor_right.brake()
    wait(500)
    readings[1] = hub.imu.heading()
    print(f"Headings: {readings}")

def clamp(val, minval, maxval):
    if val < minval:
        return minval
    if val > maxval: 
        return maxval
    return val

def move_straight_ct1():
    readings = [None, None]
    readings[0] = hub.imu.heading()

    BASE_DUTY = 50
    WAIT_TIME = 3500

    PCOEFF = 0.1

    motor_left.reset_angle(0)
    motor_right.reset_angle(0)

    motor_left.dc(BASE_DUTY)
    motor_right.dc(BASE_DUTY)

    # ── Control loop ─────────────────────────────────────────────────────────────
    timer = StopWatch()
    last_update_ms = 0
    original_ms = 0

    while True:

        time = timer.time()
        if time - original_ms > WAIT_TIME:
            break
        if time - last_update_ms < LOOP_INTERVAL_MS:
            continue
        last_update_ms = timer.time()

        # Measure how many degrees each wheel has rotated (positive = forward)
        left_rotated  = motor_left.angle()   # degrees
        right_rotated = motor_right.angle()  # degrees
        left_excess_rotated = left_rotated - right_rotated

        duty_correction = PCOEFF * left_excess_rotated
        left_duty = clamp(BASE_DUTY - duty_correction, 10, 100)
        right_duty = clamp(BASE_DUTY + duty_correction, 10, 100)

        motor_left.dc(left_duty)
        motor_right.dc(right_duty)

    motor_left.brake()
    motor_right.brake()

    readings[1] = hub.imu.heading()
    print(f"Headings: {readings}")

def move_straight_with_yaw():
    BASE_DUTY = 50
    WAIT_TIME = 3500
    PCOEFF = 1.0  # tunable: larger = more aggressive correction

    target_heading = hub.imu.heading()
    readings = [target_heading, None]

    motor_left.dc(BASE_DUTY)
    motor_right.dc(BASE_DUTY)

    timer = StopWatch()
    last_update_ms = 0

    while True:
        time = timer.time()
        if time > WAIT_TIME:
            break
        if time - last_update_ms < LOOP_INTERVAL_MS:
            continue
        last_update_ms = timer.time()

        # Positive error = robot turned right = left motor is lagging
        error = hub.imu.heading() - target_heading

        duty_correction = PCOEFF * error
        motor_left.dc(clamp(BASE_DUTY + duty_correction, 10, 100))
        motor_right.dc(clamp(BASE_DUTY - duty_correction, 10, 100))

    motor_left.brake()
    motor_right.brake()

    readings[1] = hub.imu.heading()
    print(f"Headings: {readings}")

        
def move_straight_pybricks_run():
    readings = [None, None]
    readings[0] = hub.imu.heading()
    motor_left.run(290)
    motor_right.run(290)
    wait(3500)
    motor_left.brake()
    motor_right.brake()
    wait(500)
    readings[1] = hub.imu.heading()
    print(f"Headings: {readings}")

        


#move_straight_naive()
#move_straight_ct1()
move_straight_pybricks_run()