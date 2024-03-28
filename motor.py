import sys
import time
import pygame
import RPi.GPIO as GPIO

mode = GPIO.getmode()
GPIO.setmode(GPIO.BOARD)

Forward = 26
Backward = 24
sleeptime = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
# GPIO.output(Forward, GPIO.LOW)
# GPIO.output(Backward, GPIO.LOW)

p = GPIO.PWM(32, 100)

# def forward(x):
#	GPIO.output(Forward, GPIO.HIGH)
#	print("Moving Forward")
#	time.sleep(x)
#	GPIO.output(Forward, GPIO.LOW)

# def reverse(x):
#	GPIO.output(Backward, GPIO.HIGH)
#	print("Moving Backward")
#	time.sleep(x)
#	GPIO.output(Backward, GPIO.LOW)


while True:
    p.start(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_w:
            GPIO.output(Forward, True)
            GPIO.output(Backward, False)
            GPIO.output(32, True)
            time.sleep(3)

        if event.key == pygame.K_s:
            GPIO.output(Forward, False)
            GPIO.output(Backward, True)
            GPIO.output(32, True)
            time.sleep(3)

    if event.type == pygame.KEYUP:
        GPIO.output(Forward, False)
        GPIO.output(Backward, False)

while (1):
    p.start(20)
    GPIO.output(Forward, True)
    GPIO.output(Backward, False)
    GPIO.output(32, True)
    time.sleep(3)

    p.ChangeDutyCycle(100)
    GPIO.output(Forward, True)
    GPIO.output(Backward, False)
    GPIO.output(32, True)
    time.sleep(3)

    p.ChangeDutyCycle(20)
    GPIO.output(Forward, False)
    GPIO.output(Backward, True)
    GPIO.output(32, True)
    time.sleep(3)

    p.ChangeDutyCycle(100)
    GPIO.output(Forward, False)
    GPIO.output(Backward, True)
    GPIO.output(32, True)
    time.sleep(3)
    GPIO.output(32, False)

    p.stop()
    GPIO.cleanup()
