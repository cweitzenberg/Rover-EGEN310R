import sys
import time
import pygame
import RPi.GPIO as GPIO

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Controller")

controller = pygame.joystick.Joystick(0)

done = False

mode = GPIO.getmode()
GPIO.setmode(GPIO.BOARD)

Forward = 26
Backward = 24
sleeptime = 1

GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

p = GPIO.PWM(32, 100)
servo1 = GPIO.PWM(11, 50)

p.start(20)
servo1.start(0)

while not done:

    if controller.get_button(0): #A
        pygame.draw.rect(window, (255, 0, 0), [0, 0, 200, 600])

    # if controller.get_button(1): #B?
    #     pygame.draw.rect(window, (0, 255, 0), [0, 0, 800, 600])

    # if controller.get_button(2): #Y?
    #     pygame.draw.rect(window, (0, 0, 255), [0, 0, 800, 600])

    if controller.get_button(3): #X
        pygame.draw.rect(window, (0, 0, 0), [0, 0, 800, 600])
        pygame.quit()

    if controller.get_axis(0) < 0:  # Left Joystick Horizontal
        servo1.ChangeDutyCycle(2+((controller.get_axis(0) * 180)/18))
    elif controller.get_axis(0) > 0:
        servo1.ChangeDutyCycle(2+((controller.get_axis(0) * 180)/18))

    #noah-netz
    # if controller.get_axis(1) != 1:  # Left Joystick Vertical
    #     pygame.draw.rect(window, (128, 45, 65), [0, 0, 800, 600])
    #     #print(controller.get_axis(0))

    # if controller.get_axis(2) != 0:  # Right Joystick Horizontal
    #     pygame.draw.rect(window, (128, 100, 128), [0, 0, 800, 600])
    #     #print(controller.get_axis(2))

    # if controller.get_axis(3) != 0:  # Right Joystick Vertical
    #     pygame.draw.rect(window, (128, 3, 128), [0, 0, 800, 600])
        #print(controller.get_axis(3))

    if controller.get_axis(4) != -1:  # Left Trigger
        if controller.get_axis(4)  > .95:
            p.ChangeDutyCycle(100)
        else:
            p.ChangeDutyCycle((controller.get_axis(4) + 1) * 50)
        GPIO.output(Forward, False)
        GPIO.output(Backward, True)
        GPIO.output(32, True)

    if controller.get_axis(5) != -1:  # Right Trigger
        if controller.get_axis(4) > .95:
            p.ChangeDutyCycle(100)
        else:
            p.ChangeDutyCycle((controller.get_axis(4) + 1) * 50)
        GPIO.output(Forward, True)
        GPIO.output(Backward, False)
        GPIO.output(32, True)

    if controller.get_axis(5) == -1 & controller.get_axis(4) == -1:
        GPIO.output(Forward, False)
        GPIO.output(Backward, False)
        GPIO.output(32, True)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.update()

pygame.quit()
p.stop()
servo1.stop()
GPIO.cleanup()
print("Goodbye!")
