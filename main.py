# from pythonModules.BlueDetection import getLargestBlueCenter
# from pythonModules.PID import PID

# TODO: this

from time import sleep

yaw = Servo(0)
pitch = Servo(2)

tracking = False

# idle cycle
pitch.mid()
while True:
    for i in range(Min, Max):
        yaw.set(i)
        sleep(0.1)

    for i in range(Max, Min):
        yaw.set(i)
        sleep(0.1)