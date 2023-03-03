from time import time, sleep
class PID:
    def __init__(self, P, I, D, initial) -> None:
        self.kP = P
        self.kI = I
        self.kD = D
        self.setpoint = 0
        self.output = initial
        self.lastErr = 0
        self.lastTimeExcute = time()
        self.Iprev = 0

    def update(self,setpoint):
        self.setpoint = setpoint
        curErr = self.setpoint - self.output
        Td = (time() - self.lastTimeExcute) 

        self.Iprev = self.Iprev + self.kI * (curErr - self.lastErr) * Td

        p = curErr * self.kP
        i = self.Iprev + self.kI * curErr * Td
        d = self.kD * (curErr-self.lastErr) / Td
        self.Iprev = i
        self.output = self.output + p + i + d

        self.lastErr = curErr
        self.lastTimeExcute = time()
        return self.output

import matplotlib.pyplot as plt

start = time()
timeStamps = [0]
values = [0]
pid = PID(0.2,1.5,0.0001,0)

while time() < start + 10:
    sleep(0.01)
    values.append(pid.update(50))
    timeStamps.append(time()-start)

# print(values)
plt.plot(timeStamps,values)
plt.show()

