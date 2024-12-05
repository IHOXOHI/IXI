from pyb import RTC
import struct

rtc = RTC()

results = bytearray()

class CALI:
    def __init__(self,rtc_cal=0,jump=1):
        ###variables modificables
        self.rtc_cal = rtc_cal
        self.jump = jump
        ###variables
        self.nb_cycles = 0
        self.n_period = 0
        self.t_mem = 0
        self.results = results
        ###functions
        CalState = self.CalState
        CalChange = self.CalChange
        CalJump = self.CalJump
        Cycle = self.Cycle
        AddResult = self.AddResult
        PrintResults = self.PrintResults

    def CalState(self):
        return self.rtc_cal

    def CalChange(self,rtc_cal):
        rtc.calibration(rtc_cal)
        self.rtc_cal = rtc_cal
        return self.rtc_cal

    def CalJump(self):
        return self.jump

    def StartCycle(self):
        rtc.calibration(self.rtc_cal)
        t_mem = rtc.datetime()[7]
        self.t_mem = t_mem

    def Cycle(self):
        t = rtc.datetime()[7]
        if self.n_period == 1:
            self.nb_cycles += 1
            if t != self.t_mem:
                result = [self.rtc_cal,self.nb_cycles]
                self.AddResult(result)
                if t > self.t_mem:
                    self.rtc_cal += self.jump
                else:
                    self.rtc_cal -= self.jump
                self.CalChange(self.rtc_cal)
                self.nb_cycles = 0
                self.t_mem = t
                self.n_period = 0
        else:
            if t != self.t_mem:
                self.t_mem = t
                self.n_period = 1

        return self.nb_cycles

    def AddResult(self,result):
        for i in range(2):
            data = result[i]
            data = struct.pack(">H", data)
            self.results.extend(data)

    def PrintResults(self):
        resultat = []
        nb = (len(self.results))
        for i in range(0, nb, 2):
            j = i + 2
            data = struct.unpack(">H", self.results[i:j])
            resultat.append(data)
        return resultat
