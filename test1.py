import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)

trigg=23
echo=24

dht=Adafruit_DHT.DHT11
pin=4
with open ("test2.txt","a") as file:

##########################################################

    GPIO.setup(trigg, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    GPIO.output(trigg,True)
    time.sleep(0.00001)
    GPIO.output(trigg,False)

    while GPIO.input(echo)==0:
        start=time.time()
    while GPIO.input(echo)==1:
        end=time.time()

    duration=end-start
    dist=duration*17150
    dist=round(dist,2)
