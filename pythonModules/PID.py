from time import time, sleep
class PID:
    def __init__(self, P, I, D, initial, forceStep:int = None) -> None:
        self.kP = P
        self.kI = I
        self.kD = D
        self.setpoint = 0
        self.output = initial
        self.lastErr = 0
        self.lastTimeExcute = time()
        self.Iprev = 0
        self.forceStep = forceStep

    def update(self,setpoint):
        self.setpoint = setpoint
        curErr = self.setpoint - self.output
        Td = (time() - self.lastTimeExcute) if self.forceStep == None else (self.lastTimeExcute+self.forceStep - self.lastTimeExcute)

        self.Iprev = self.Iprev + self.kI * (curErr - self.lastErr) * Td

        p = curErr * self.kP
        i = self.Iprev + self.kI * curErr * Td
        d = self.kD * (curErr-self.lastErr) / Td
        self.Iprev = i
        self.output = self.output + p + i + d

        self.lastErr = curErr
        self.lastTimeExcute = self.forceStep + self.lastTimeExcute if self.forceStep != None else time()
        return self.output

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # start = time()
    timeStamps = [0]
    values = [0]
    step = 0.5
    start = time()
    pid = PID(0.75,0.0006,0.01, 0)
    cur = 0
    for i in range(100):
        sleep(0.1)
        values.append(pid.update(50))
        timeStamps.append(time()-start)
        # cur += step

    # print(values)
    plt.plot(timeStamps,values)
    plt.show()

