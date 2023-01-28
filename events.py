import pygame as pygame

playerInput: list = [0, 0]


def HandleEvents():

    global playerInput
    playerInput = UpdateInput()

    print(playerInput)

    for event in pygame.event.get():
        CheckQuit(event)


def CheckQuit(event: pygame.event.Event):
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()


def UpdateInput():
    newInput: list = [0, 0]

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        newInput[0] -= 1
    if keys[pygame.K_RIGHT]:
        newInput[0] += 1
    if keys[pygame.K_UP]:
        newInput[1] += 1
    if keys[pygame.K_DOWN]:
        newInput[1] -= 1

    return newInput