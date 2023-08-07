# imports
import pygame
from video_player import play_video
from classes import TButton, TDice, TKonto, TLabel, screen_create, colors

# library initializations
pygame.init()
pygame.font.init()


# variables
game_active = True
dice_thrown = False
player_choice = 1


# objects
# konto
konto = TKonto(100)

# labels
konto_label = TLabel(f"Kontostand: {konto.getBalance()}", (50, 50))
player_choice_label = TLabel(f"Ihre Glückszahl: {player_choice}", (50, 160))

labels = [konto_label, player_choice_label]

# dices
d1 = TDice()
d2 = TDice()
d3 = TDice()

dices = [d1, d2, d3]

# buttons
throw_button = TButton(colors["WEISS"], (250, 50), 100, 50, "werfen")
change_screen_button = TButton(colors["WEISS"], (400, 50), 100, 50, "Lootbox")
button1 = TButton(colors["WEISS"], (200, 330), 50, 50, "1")
button2 = TButton(colors["WEISS"], (270, 330), 50, 50, "2")
button3 = TButton(colors["WEISS"], (340, 330), 50, 50, "3")
button4 = TButton(colors["WEISS"], (200, 400), 50, 50, "4")
button5 = TButton(colors["WEISS"], (270, 400), 50, 50, "5")
button6 = TButton(colors["WEISS"], (340, 400), 50, 50, "6")

buttons = [throw_button, change_screen_button, button1, button2, button3, button4, button5, button6]


# create screen
background = pygame.image.load(f"assets/R.jpg")
background = pygame.transform.smoothscale(background, (640, 480))
screen = screen_create((640, 480), "Chuck a Luck", background)


# font loader
font = pygame.font.SysFont("Arial", 32)


# clock for later fps lock
clock = pygame.time.Clock()


# main loop
while game_active:

    # get mouse-position
    mouse_pos = pygame.mouse.get_pos()

    # loop to check for inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if throw_button.isOver(mouse_pos):
                play_video()
                dice_thrown = True
                for dice in dices:
                    dice.throw_dice()

            for button in buttons[2:7]:
                if button.isOver(mouse_pos):
                    player_choice = button.text

    # win management
    if dice_thrown:
        for dice in dices:
            if dice.get_number() == int(player_choice):
                konto.addCoin(1)

            else:
                konto.removeCoin(1)

    # labeltext updates
    konto_label.update_text(f"Kontostand: {konto.getBalance()}")
    player_choice_label.update_text(f"Ihre Glückszahl: {player_choice}")

    # clearing screen
    screen.blit(background, (0, 0))

    # drawing dices,buttons and labels
    for i, dice in enumerate(dices):
        dice.show_pic(screen, (150 + i * 100, 200))

    for button in buttons:
        button.draw(screen, font)

    for label in labels:
        label.draw(screen, font)

    # part of win management
    dice_thrown = False

    # update the screen
    pygame.display.update()

    # refresh rate in fps
    clock.tick(60)

pygame.quit()
