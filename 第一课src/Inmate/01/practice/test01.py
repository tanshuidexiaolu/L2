import pygame

while True:
    pygame.init()
    #请在下方书写你的代码

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
