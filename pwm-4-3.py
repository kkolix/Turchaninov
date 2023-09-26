import RPi.GPIO as gp
gp.setmode(gp.BCM)
gp.setup(24, gp.OUT)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
gp.setup(dac, gp.OUT)
pwm=gp.PWM(24, 1000)
pwm.start(0)

try:
    while True:
            DutyCycle=int(input())
            pwm.ChangeDutyCycle(DutyCycle)
            print("{:.2f}".format(DutyCycle*3.3/100))

finally:
    gp.output(24, 0)
    gp.output(dac, 0)
    gp.cleanup()