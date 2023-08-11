import lootbox
import chuck_a_luck
from classes import *
from objects import buttons

pygame.init()
pygame.font.init()


# variables
run = True
dice_thrown = False
player_choice = 1


# buttons

# create screen
background = pygame.image.load(f"assets/menu_background.jpg")
background = pygame.transform.smoothscale(background, (640, 480))
screen = screen_create((640, 480), "Menu", (0, 0, 0), background)


# font loader
font = pygame.font.SysFont("Arial", 32)


# clock for later fps lock
clock = pygame.time.Clock()


# main loop
while run:
    # get mouse-position
    mouse_pos = pygame.mouse.get_pos()

    # loop to check for inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if buttons[__name__]["chuck_a_luck_button"].isOver(mouse_pos):
                chuck_a_luck.init()

            elif buttons[__name__]["lootbox_button"].isOver(mouse_pos):
                lootbox.init()

            pygame.display.set_caption("Menu")

    screen.blit(background, (0, 0))

    for button in buttons[__name__]:
        buttons[__name__][button].draw(screen, font)

    # update the screen
    pygame.display.update()

    # refresh rate in fps
    clock.tick(60)

# konto.save_profile()
pygame.quit()
