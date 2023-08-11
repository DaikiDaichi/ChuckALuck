# imports
import pygame
from objects import konto, buttons, labels, dices
from video_player import play_video
from classes import screen_create


def init():
    # library initializations
    pygame.init()
    pygame.font.init()

    # create screen
    info_text = pygame.image.load("assets/chuck_a_luck_info.png")
    background = pygame.image.load("assets/chuck_a_luck_background.jpg")
    background = pygame.transform.smoothscale(background, (640, 480))
    screen = screen_create((640, 480), "Chuck a Luck", (0, 0, 0), background)

    # font loader
    font = pygame.font.SysFont("Arial", 32)

    # clock for later fps lock
    clock = pygame.time.Clock()

    # variables
    game_active = True
    dice_thrown = False
    player_choice = 1

    # main loop
    while game_active:

        # get mouse-position
        mouse_pos = pygame.mouse.get_pos()

        # loop to check for inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons["chuck_a_luck"]["throw_button"].isOver(mouse_pos):
                    play_video(screen)
                    dice_thrown = True
                    for dice in dices:
                        dices[dice].throw_dice()

                elif buttons["chuck_a_luck"]["return_button"].isOver(mouse_pos):
                    game_active = False

                for i in range(1, 7):
                    if buttons["chuck_a_luck"][f"button{i}"].isOver(mouse_pos):
                        player_choice = buttons["chuck_a_luck"][f"button{i}"].text

        # win management
        if dice_thrown:
            for dice in dices:
                if dices[dice].get_number() == int(player_choice):
                    konto.addCoin(1)

                else:
                    konto.removeCoin(1)

        # labeltext updates
        labels["konto_label"].update_text(f"Kontostand: {konto.getBalance()}")
        labels["player_choice_label"].update_text(f"Ihre Glückszahl: {player_choice}")

        # clearing screen
        screen.blit(background, (0, 0))

        # drawing dices,buttons and labels
        for i, dice in enumerate(dices):
            dices[dice].show_pic(screen, (150 + i * 100, 200))

        for button in buttons["chuck_a_luck"]:
            buttons["chuck_a_luck"][button].draw(screen, font)

        for label in labels:
            labels[label].draw(screen, font)

        if buttons["chuck_a_luck"]["info_button"].isOver(mouse_pos):
            # add alpha
            alpha_surf = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            alpha_surf.set_alpha(230)
            alpha_surf.blit(info_text, (0, 0))
            screen.blit(alpha_surf, (0, 0))

        # part of win management
        dice_thrown = False

        # update the screen
        pygame.display.update()

        # refresh rate in fps
        clock.tick(60)
