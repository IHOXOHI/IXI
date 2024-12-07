import uasyncio
from pyb import RTC

rtc = RTC()

rtc.calibration(-171)

n = 0
t_mem = 0

async def main():
    global n, t_mem
    while 1:
        if n == 0:
            t = rtc.datetime()[7]
            t_mem = t
            n = 1
        if n == 1:
            t = rtc.datetime()[7]
            if t != t_mem:
                n = 2
                t_mem = t
        else:
            n+=1
            t = rtc.datetime()[7]
            if t != t_mem:
                print(n)
                break
        await uasyncio.sleep_ms(1000)

uasyncio.run(main())
