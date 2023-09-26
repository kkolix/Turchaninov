import sys
import RPi.GPIO as gp
dac = [8, 11, 7, 1, 0, 5, 12, 6]
gp.setmode(gp.BCM)
gp.setup(dac, gp.OUT)
def binary(a, n):
    return [int (m) for m in bin(a)[2:].zfill(n)]
try:
    while (True):   
        a = input ()
        if a=='q':
            sys.exit()
        elif a.isdigit() and int(a)%1==0 and 0<=int(a)<=255:
            gp.output(dac, binary(int(a), 8))
            print("{:.4f}".format(int(a)/256*3.3))
        elif not a.isdigit():
            print ('Pls input number 0-255')
        elif int(a) > 255:
            print('input 0-255')
except ValueError:
    print ('input 0-255')
finally:
    gp.output(dac, 0)
    gp.cleanup()