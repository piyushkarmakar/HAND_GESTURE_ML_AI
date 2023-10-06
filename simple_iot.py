#!pip install RPI


import RPI.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarning(False)
class Motor():
    def __init__(self,Ena,In1,In2):
        self.Ena=Ena
        self.In1=In1
        self.In2=In2
        GPIO.setup(self.Ena,GPIO.OUT)
        GPIO.setup(self.In1,GPIO.OUT)
        GPIO.setup(self.In2,GPIO.OUT)
        pwm=GPIO.PWM(self.Ena,100)
        pwm.start(0)
    def moveF(self,x=50,t=0):
        GPIO.output(self.In1,GPIO.LOW)
        GPIO.output(self.In2,GPIO.HIGH)
        self.pwm.ChangeDutyCycle(x)
        sleep(t)
    def moveB(self,x=50,t=0):
        GPIO.output(self.In1,GPIO.High)
        GPIO.output(self.In2,GPIO.LOW)
        self.pwm.ChangeDutyCycle(x)
        sleep(t)
    def stop(self,t=0):
        self.pwm.ChangeDutyCycle(0)
        sleep(t)
    
        
        
m1=Motor(2,3,4)
while True:
    m1.moveF(30,2)
    m1.stop(2)
    m1.moveB(100,2)
    