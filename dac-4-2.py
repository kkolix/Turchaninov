import sys
import RPi.GPIO as gp
from time import sleep
dac = [8, 11, 7, 1, 0, 5, 12, 6]
gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)
def dec2bin(a, n):
    return [int (m) for m in bin(a)[2:].zfill(n)]

try:
    while (True):  
        z = input()
        if z=='q':
            sys.exit()
        elif not z.isdigit():
            print ('pls input number')
            sys.exit()
        a=int(z)/256/2
        for i in range(256):
                gp.output(dac, dec2bin(i, 8))
                sleep(a)
        for i in range (255, -1, -1):
                gp.output(dac, dec2bin(i, 8)) 
                sleep(a)


finally:
    gp.output(dac, 0)
    gp.cleanup()