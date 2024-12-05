import IXI
import uasyncio

cali = IXI.CALI(rtc_cal=500,jump=50)

number_cycles = 0

async def main():
    jumpi = cali.CalJump()
    global calib_indice, number_cycles
    calib_indice = cali.CalState()
    print("Indice de calibration: {}\nJump: {}".format(calib_indice,jumpi))
    n = 0
    while number_cycles < 20: ###you have to change it to yours wishes
        if n == 0:
            cali.StartCycle()
            n = 1
        else:
            number_cycles = cali.Cycle()
        await uasyncio.sleep_ms(1000)
    data = cali.PrintResults()
    print(data)
uasyncio.run(main())
