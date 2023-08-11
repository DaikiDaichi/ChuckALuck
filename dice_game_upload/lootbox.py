"""
Lootboxen:

Mehrere Knöpfe (vllt. 3) + return_button
Lootboxen Bilder (3 verschd.)
bei klick auf Knopf öffne Lootbox
zeige assets/chest.mpv
zeige bild von loot (niet [als ticket], win [als muenzen])
"""

import pygame
from random import randint
from objects import konto, buttons
from video_player import play_video
from classes import screen_create


def init():
    pygame.init()
    pygame.font.init()

    # objects
    # buttons

    # create screen
    background = pygame.image.load(f"assets/lootbox_background.jpg")
    background = pygame.transform.smoothscale(background, (640, 480))
    screen = screen_create((640, 480), "Lootbox", (0, 0, 0), background)

    # font loader
    font = pygame.font.SysFont("Arial", 32)

    # clock for later fps lock
    clock = pygame.time.Clock()

    # variables
    game_active = True

    # main loop
    while game_active:

        # get mouse-position
        mouse_pos = pygame.mouse.get_pos()

        # loop to check for inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons["lootbox"]["lootbox_1_button"].isOver(mouse_pos):
                    play_video(screen, "chest.mkv")
                    konto.removeCoin(5)
                    konto.addCoin(randint(1, 10))

                elif buttons[__name__]["return_button"].isOver(mouse_pos):
                    game_active = False

        # clearing screen
        screen.blit(background, (0, 0))

        # drawing buttons
        for button in buttons[__name__]:
            buttons[__name__][button].draw(screen, font)

        # update the screen
        pygame.display.update()

        # refresh rate in fps
        clock.tick(60)
