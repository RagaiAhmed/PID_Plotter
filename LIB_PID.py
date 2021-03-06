"""
USING PID Library for comparison
"""
from Helpers import sensor_read
from matplotlib import pyplot
from time import sleep
from simple_pid import PID
pid = PID(1, 0, 0, setpoint=100)


if __name__ == "__main__":
    res = -1  # Triggers initial sensor reading

    x= []
    y = []
    for _ in range(5):  # Main execution loop
        sleep(1)

        reading = sensor_read(res)
        res = pid(reading)
        x.append(_+1)  # Time
        y.append(reading)

    pyplot.plot(x,y)
    pyplot.show()

