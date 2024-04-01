import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Controller")

controller = pygame.joystick.Joystick(0)
mysound1 = pygame.mixer.Sound('RoadRunnerBeepBeep.wav')
mysound2 = pygame.mixer.Sound('fireflies.wav')

done = False

while not done:
    if controller.get_button(0): #A
        pygame.draw.rect(window, (255, 0, 0), [0, 0, 200, 600])
    if controller.get_button(1): #B
        pygame.draw.rect(window, (0, 255, 0), [0, 0, 800, 600])
        mysound1.play()
        print("sound")
    if controller.get_button(2): #X
        pygame.draw.rect(window, (0, 0, 255), [0, 0, 800, 600])
        mysound2.play()
    if controller.get_button(3): #Y
        pygame.draw.rect(window, (0, 0, 0), [0, 0, 800, 600])
        pygame.quit()
    if controller.get_axis(0) < 0:  # Left Joystick Horizontal
        pygame.draw.rect(window, (44, 0, 128), [0, 0, 800, 600])
        #print("turning left")
        #print(controller.get_axis(0)*(-100))
    elif controller.get_axis(0) > 0:
        pygame.draw.rect(window, (44, 0, 128), [0, 0, 800, 600])
        #print("turning right")
        #print(controller.get_axis(0) * (100))
    # if controller.get_axis(1) != 1:  # Left Joystick Vertical
    #     #pygame.draw.rect(window, (79, 49, 128), [0, 0, 800, 600])
    #     print(controller.get_axis(0))
    # if controller.get_axis(2) != 0:  # Right Joystick Horizontal
    #     #pygame.draw.rect(window, (45, 45, 128), [0, 0, 800, 600])
    #     print(controller.get_axis(2))
    # if controller.get_axis(3) != 0:  # Right Joystick Vertical
    #     #pygame.draw.rect(window, (128, 0, 3), [0, 0, 800, 600])
    #     print(controller.get_axis(3))
    if controller.get_axis(4) != -1:  # Left Trigger
        if controller.get_axis(4) > .95:
            (128, 128, 128)
        else:
            pygame.draw.rect(window, ((controller.get_axis(4) + 1) * 64, (controller.get_axis(4) + 1) * 64, (controller.get_axis(4) + 1) * 64), [0, 0, 800, 600])
        print(controller.get_axis(4))
    if controller.get_axis(5) != -1:  # Right Trigger
        pygame.draw.rect(window, (45, (controller.get_axis(5) + 1) * 64, 128), [0, 0, 800, 600])
        #print(controller.get_axis(5))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.update()

pygame.quit()