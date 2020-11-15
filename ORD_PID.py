"""
Implementing PID from scratch
"""
from Helpers import sensor_read
from matplotlib import pyplot

ltime = 0
lval = None

Kp =.9
Ki = .00001
Kd = 0.05

ti = 0

time_diff = 0.05


def normal_pid_exec(set_point, current):
    """
        returns PID corrected value for given set_point and current value
    :param set_point:  The target set point
    :param current:  Current recorded value

    global variables used
    Kp:  Gain for Proportional part
    Ki:  Gain for Integral part
    Kd:  Gain for Derivative part
    ltime:  Last call time
    lval:  Last call "current" value
    ti:  total integral so far
    :return:
    """
    global ti, lval, ltime
    new = 0
    current_time = ltime + time_diff
    e = (set_point - current)  # Error is difference between current and the set point

    if ltime is not None:
        dt = current_time - ltime  # Change in time

        if lval is not None:
            dv = (e - lval)

            new += (dv / dt) * Kd  # Adding derivative part of PID

        ti += e * dt  # Accumulating values of errors (integral)

        new += ti * Ki  # Adding integral part in PID

    new += e * Kp  # Adding proportional part in PID

    # Storing current conditions for next call
    lval = e
    ltime = current_time

    return new


if __name__ == "__main__":
    res = -1  # Triggers initial sensor reading
    set_point = 100  # Set point is 100

    x = []
    y = []
    for _ in range(int(100/time_diff)):  # Main execution loop
        reading = sensor_read(res)
        res = normal_pid_exec(set_point, reading)
        x.append(ltime)
        y.append(reading)

    pyplot.plot(x, y)
    pyplot.show()
