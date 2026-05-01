from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import StopWatch
import math

# ── Robot setup ──────────────────────────────────────────────────────────────
hub = PrimeHub()

# positive_direction means: which way is "positive" rotation for this motor?
# The left motor is mounted facing the other way, so we flip it here.
# After this, positive angle/duty = forward for BOTH motors.
motor_left  = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.E, Direction.CLOCKWISE)

# ── Mission parameters ───────────────────────────────────────────────────────
DISTANCE_MM       = 500   # how far to travel (mm)
WHEEL_DIAMETER_MM = 56    # wheel diameter (mm)

# ── Controller settings ──────────────────────────────────────────────────────
BASE_DUTY          = 40   # feedforward power (%, 0-100)
P_GAIN             = 0.8  # how aggressively to correct heading errors
MAX_HEADING_ADJUST = 20   # cap on heading correction (%)
LOOP_INTERVAL_MS   = 20   # how often to update the loop (ms)

# ── Calculate target wheel rotation ──────────────────────────────────────────
# Distance = (degrees / 360) * circumference, so:
# degrees = (distance / circumference) * 360
wheel_circumference_mm = math.pi * WHEEL_DIAMETER_MM
target_degrees = (DISTANCE_MM / wheel_circumference_mm) * 360

# ── Reset motor angles and start moving ──────────────────────────────────────
motor_left.reset_angle(0)
motor_right.reset_angle(0)

motor_left.dc(BASE_DUTY)
motor_right.dc(BASE_DUTY)

# ── Control loop ─────────────────────────────────────────────────────────────
timer = StopWatch()
last_update_ms = 0

while True:

    # Skip this iteration if not enough time has passed since last update
    if timer.time() - last_update_ms < LOOP_INTERVAL_MS:
        continue
    last_update_ms = timer.time()

    # Measure how many degrees each wheel has rotated (positive = forward)
    left_rotated  = motor_left.angle()   # degrees
    right_rotated = motor_right.angle()  # degrees

    # Exit when the average rotation reaches the target
    average_rotated = (left_rotated + right_rotated) / 2
    if average_rotated >= target_degrees:
        break

    # Heading error: if right > left, the robot has veered left
    heading_error = right_rotated - left_rotated  # degrees

    # P controller: scale the error into a correction value, then clamp it
    heading_adjust = P_GAIN * heading_error
    if heading_adjust >  MAX_HEADING_ADJUST:
        heading_adjust =  MAX_HEADING_ADJUST
    if heading_adjust < -MAX_HEADING_ADJUST:
        heading_adjust = -MAX_HEADING_ADJUST

    # Apply correction: slow the leading side, speed up the lagging side
    left_duty  = BASE_DUTY + heading_adjust
    right_duty = BASE_DUTY - heading_adjust

    # Clamp duty cycles to valid motor range (%)
    left_duty  = max(0, min(100, left_duty))
    right_duty = max(0, min(100, right_duty))

    motor_left.dc(left_duty)
    motor_right.dc(right_duty)

# ── Stop ─────────────────────────────────────────────────────────────────────
motor_left.stop()
motor_right.stop()
