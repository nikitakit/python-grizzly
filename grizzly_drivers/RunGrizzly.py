from libgrizzlyusb import *
from xbox_read import event_stream

g = GrizzlyUSB()
grizzly = Grizzly(g)
grizzly.setMode(ControlMode.NO_PID, DriveMode.DRIVE_BRAKE)
inputs = event_stream(4000)

for event in inputs:
    if event.key == "Y2":
        throttle = int(event.value) / 327
        grizzly.setSpeed(throttle)
