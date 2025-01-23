###   IXI   ###
#   The result is based on rtc.datetime[7], so the ms counter with 255 graduations (999ms), so 4ms of granularity there.
####   a result of 1000 means: 1000 sec to wait for have a delay of 4ms. So 4 us of precision in time.
#Pybstick from MCHOBBY (6mA)
Pybstick_0 = [10, 17, 4, 3, 34, 27, 11, 28, 7, 21]
Pybstick_full, [[0,14], [-115,1238], [-116,-1109], [-115,1238], [-115,1233], [-115,1234], [-115,1233], [-115,1233], [-115,-1028], [-115,-1234], [-115,-36], [-115,1240], [-113,1139], [-113,1108], [-113,1233], [-113,369], [-111,696], [-112,772], [-114,1119], [-114,1233], [-114,1225], [-114,561]]
Pybstick_115 = [1238, -1109, 1238, 1233, 1234, 1233, 1233, -1028, -1234, -36, 1240]
Pybstick_localtime = [3197, 3197]

#Pybstick2
Pybstick2_0 = [4, 37, 26, 30, 24, 8, 39]
Pybstick2_full = [[-115,-533], [-115,-657], [-120,-304], [-113,-388], [-116,-645], [-111,856], [-111,1233], [-111,1232], [-111,1231], [-111,1231], [-111,1225], [-111,1108], [-111,1214], [-111,1214], [-111,1227], [-111,1226]]
Pybstick2_111 = [856, 1233, 1232, 1231, 1231, 1225, 1108, 1214, 1214, 1227, 1226, 1233, 667, 1197,1226]
Pybstick2_localtime = [3210, 3211]

#Pyb405 from Garatronic (20mA)
Pyb405_0 = [-118, -169, -156]
Pyb405_full = [[0,-50], [100,-33], [-100,41], [-50,34], [50,-32], [-20,1751], [-22,70], [-18,-2011], [-19,-8167], [-19,-2012], [-19,6113], [-19,622], [-19,16311], [-21,1594], [-21, 1692], [-21, 863]]
#Pyb405_localtime: more than 20000 hours...

#Feather F405 from Adafruit (20mA)
F405_0 = [-10, -5, -27, -41, -20, -23, -30]
F405_full = [[0,17], [100,10], [-100,253], [-200,43], [-150,91], [-75,120], [-125,179], [-115,356], [-110,723], [-105,3423], [-106,368], [-104,1935], [-103,382], [-107,553], [-105,3906], [-105,3906], [-105,1933], [-105,3905], [-105,2498], [-105,1091], [-105,1909], [-105,-3852], [-105,-1907], [-105,-3904], [-105,-3875], [-105,-3876], [-105,-3872], [-105,-1898], [-105,-5838], [-105,-3868]]
F405_105, = [3906, 3906, 1933, 3905, 2498, 1091, 1909, -3852, -1907, -3904, -3875, -3876, -3872, -1898, -5838, -3868]
#F405_localtime = more than 80000 cycles...

#F405 2
F4052_full = [[-105,77], [105,-19], [-100,298], [-90,-738], [-93,-5875], [-93,9547], [-93,448], [-92,-3903], [-92,3903], [-92,-1737], [-92,-1617], [-92,-1157], [-92,-1934], [-92,2030], [-92,-115], [-92,-1594], [-92,-1927], [-91,-1323], [-91,-1757], [-91,-1182], [-91, -5], [-90,-190], [-95,1704], [-95,1779], [-95,95], [-94,-5803], [-94,-5803], [-94,-7767], [-94,1525], [-94,1291], [-94,-1501], [-94,3132], [-94, 3602], [-94,915], [-94,1231], [-94,344]]
F4052_94, = [-5803,-5803,-7767,1525,1291,-1501, 3132, 3602, 915, 1231, 344]

#Pyboard china (20mA)
Pyb_ch_full = [[0,11], [100,140], [200,-7], [150,-193], [130,-1614], [125,13], [127,659], [128,-3817], [129,1432], [128,108], [129,-6115], [129,-2009], [129,-2009], [129,-4062], [129,8], [129,-4054]]
Pyb_ch_129 = [1432,6115,2009,2009,4062, 8,4054]
Pyb_ch_130 = [4061,2007,2007,4060,2006,1949,1948,4001,4000,3998,3998,6149,3694]

#Pyboard china 2
Pyboard_ch2_full = [[130,-20], [-130,36], [-50,239], [-31,-151], [-42,474], [-40,898], [-38,1371], [-30,-500], [-35,-1962], [-37,5581], [-37,1434], [-36,918], [-35,-1386, [-35,342], [-35,-8104], [-37,1761], [-37,-1451], [-37,-1069], [-34,-2303], [-34,-1950], [-34,-1950], [-34,-1949], [-34,-1693], [-34,-1950], [-34,-1948], [-34,-1948], [-34,-1947], [-34,-1946], [-34,-2044], [-34,-1946], [-34,-3995], [-34,-1945], [-34,-3994]]
Pyboard_ch2_34 = [-2303, -1950, -1950, -1949, -1693, -1950, -1948, -1948, -1947, -1946, -2044, -1946, -3995, -1945, -3994]
#Pyboard_localtime = to do... for moment more than 30000

#Pyboard uk (20mA)
Pyboard_uk_0 = [-6, -24, -22, -22, -9, -8, -21, -12]
Pyboard_uk_full = [[-181,1229], [-179,1929], [-177,1154], [-171,668], [-183,250], [-190,575], [-150,-74], [-165,-247], [-169,-314], [-170,-288], [-171,-99], [-179,-2014], [-179,-2363], [-179,-1897], [-179,-2014], [-179,-2014], [-179,-2042], [-179,-459], [-179,-1055], [-179,2042], [-179,-1817], [-178,-1991], [-178,-1200], [-178,-571], -[182,1524], [-182, 231], [-180,-1943], [180,3]]
#Done before, without signs: [[181,174], [180,1468], [179,433], [178,1106], [176,439], [177,330], [174,267], [175,369], [181,1185], [183,1862], [185,198], [184,185], [182,1426], [181,2019], [183,621], [186,258]]

#Pybnano (7mA)
Pybnano_full = [[-31,-1149], [-35,254], [-33,731], [-32,199], [-31,-1149], [-30,-1150], [-31,1150], [-31,284], [-30,-1143], [-30,1306], [-30,-1130], [-30,90], [-30,-1144], [-30,978], [-30,-1250], [-30, -1313], [-30,-1192]]
Pybnano_30 = [-1150, -1143, 1306, -1130, 90, -1144, 978, -1250, -1313, -1192]
Pybnano_29 = [-1313, -1132, -1304, 475, -1240, 1303, -1132, -1134, -1134, -1132, -1306, -1135]
Pybnano_localtime = [3351]

#Pybnano2
Pybnano2_0 = [-14, -92, -62, -42, -22]
Pybnano2_full = [[-35,396], [-37,715], [-33,1312], [-31,1191], [-29,108], [-32,1141], [-29,651], [-28,222], [-34,1252], [-36,821], [-35,1167], [-33,1061], [-36,1021], [-33,1141], [-30,939], [34,1252], [34,289], [33,1312], [32,1192], [32,1192], [-32,-1139], [-33,-1252], [-34,231], [-33,-1305], [-32,-1127], [-32,-1127], [-32,-1128], [-32,-1129], [-32,-1127], [-32,-1129], [-32,-1129], [-32,-1128], [-32,-1127], [-32,-1129], [-32,-1129]]
Pybnano2_32 = [-1127, -1127, -1128, -1129, -1127, -1129, -1129, -1128, -1127, -1129, -1129]

#Black-Pill F411ceu6 (9mA)
BP411_0 = [-6, -4, -11, -17, -7, -6]
BP411_full, [[0, -21,], [100, -14], [-100, -31], [-200, -121], [-300,19], [-222, 172], [-215,-1240], [-215,-1272], -[215,-1240], [-215,-320], [-211,-361, [-216,-1243], [-216,-1240], [-216,-1367], [-216,-1298], [-216,-1218], [-216,-1184], [-216,-1035], [-216,-1123], [-216,-1367], [-216,-1240], [-216,1177], [-216,-1235], [-216,-1235], [-216,-502], [-216,-575], [-216,-1240]]
BP411_216 = [-1243, -1240, -1367, -1298, -1218, -1184, -1035, -1123, -1367, -1240, -1177, -1235, -1235, -502, -575, -1240]
BP411_localtime = [3543]


########################################################################################################################################
#####################################################################################################################################
###   IXI6   ### see the script below
#with machine.RTC() #No calibration
#The result is based on rtc.datetime[6], so the counter of second, so 1s of granularity. 255 less precise than before, there!
####   a result of 1000 means: 1000 sec to wait for have a delay of 1s. So 1 ms of precision in time.

#ARDUINO GIGA (82mA)
Giga = [42, 42, 41, 41]
#Giga_localtime = to do... 
#Giga_IMI = infinite!

#Feather esp32S3 from Unexpected Makers (64mA)
UMFeatherS3 = [577,102,577,102,583,585]
UMFeatherS3_localtime = [102, 102, 102]

#Pico from Raspberry (17mA)
Pico = [1231,771,883,965,1087,902,1113,1028,1022,1129,3,1081]
Pico_localtime = [1023, 1010]

#Pico2 from raspberry(15mA):
Pico2 = [1428,1774,2160,1556,1560,1538,1546,1555,1522,1568,

#PicoLipo 16M from Pimoroni (22mA)
Pimo = [1141,1261,1072,1335,1058,1078,1016,899,1028,845,1093,863,939]
Pimo_localtime = [789,895]

#Esp32 with lora and oled from liligo (32mA)
Liligo = [102, 102, 102, 102, 102]
Liligo_localtime = [102, 102]

#Feather M4 express from Adafruit (9mA)
FeatherM4 = [1256,1866,1251,637,1292,1777,2328,2359,991,1002]
FeatherM4_localtime = [1192, 1379]

#RT1101 from Olimex (53mA)
RT1101 = [15436, 14784]
#RT1101_localtime = to do... for moment more than 30000

#Teensy 4.1 (72mA)
#Teensy_full = more than 86400 cycles...
#Teensy_localtime = to do?

#Lolin32 (30mA)
Lolin32 = [1001, 1001, 920, 1001, 847, 696, 1144]
Lolin32_localtime = [962]





####################################################################################
#### IXI6.py ####  the script for boards without ms counter
import uasyncio
from machine import RTC

rtc = RTC()
n = 0
t_mem = 0

async def main():
    global n, t_mem
    n,t = 0, 0
    while 1:
        if ((t == 59) and (t_mem == 59)):
                t_mem = -1
        if n >= 2:
            n+=1
            t = rtc.datetime()[6]
            t_mem += 1
            if t != t_mem:
                print(n)
                break
        if n == 1:
            t = rtc.datetime()[6]
            t_mem += 1
            if t != t_mem:
                n =2
                t_mem = t
        if n == 0:
            t = rtc.datetime()[6]
            t_mem = t
            n = 1
        await uasyncio.sleep_ms(1000)

uasyncio.run(main())


