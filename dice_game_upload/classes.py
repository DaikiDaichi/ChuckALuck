# import json
from random import randint
import pygame

pygame.init()
pygame.font.init()

colors = {
    "ORANGE": (255, 140, 0),
    "ROT": (255, 0, 0),
    "GRUEN": (0, 255, 0),
    "SCHWARZ": (0, 0, 0),
    "WEISS": (255, 255, 255),
    "TURKIS": (137, 225, 209)
}


def screen_create(resolution=(640, 480), window_title="", color=(0, 0, 0), picture=None):
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption(window_title)

    # when no image or wrong datatype is given, the screen will be filled with the given color (default: black)
    try:
        if picture is not None:
            screen.blit(picture, (0, 0))
        else:
            screen.fill(color)

    except TypeError:
        screen.fill(color)
    return screen


class TLabel:
    def __init__(self, text, location=(0, 0)):
        self.text = text
        self.location = location

    def update_text(self, new_text):
        self.text = new_text

    def draw(self, surface, font):
        label = font.render(self.text, False, colors["TURKIS"])
        surface.blit(label, self.location)


class TDice:
    def __init__(self):
        self.number = randint(1, 6)

    def throw_dice(self):
        self.number = randint(1, 6)
        return self.number

    def get_number(self):
        return self.number

    def show_pic(self, surface, location=(80, 200)):
        img = pygame.image.load(f"assets/dice_{self.number}.png")
        width, height = img.get_size()
        img = pygame.transform.smoothscale(img, (width / 6, height / 6))
        surface.blit(img, location)


class TKonto:
    def __init__(self, balance=0, owner="admin"):
        self.__balance = balance
        self.__owner = owner

    def addCoin(self, amount):
        self.__balance += amount

    def removeCoin(self, amount):
        self.__balance -= amount

    def getBalance(self):
        return self.__balance

    def getAttr(self):
        return self.__owner, self.__balance

    '''
    def save_profile(self):
        with open("assets/profile.json", "r") as readfile:
            json_data = json.load(readfile)
            for x, i in enumerate(json_data["konten"]):
                if i["owner"] == self.getAttr()[0]:
                    print(json_data["konten"][x])
                    del json_data["konten"][x]

            if self.getAttr()[0] != "Demo":
                json_data["konten"].append({"owner": self.getAttr()[0], "balance": self.getAttr()[1]})

        with open("assets/profile.json", "w") as wfile:
            json.dump(json_data, wfile)
    '''


class TButton:
    font = pygame.font.Font(None, 36)

    def __init__(self, color=(0, 255, 0), pos=(0, 0), width=20, height=5, text=''):
        self.color = color
        self.x, self.y = pos
        self.width = width
        self.height = height
        self.text = text

    def draw(self, surface, outline=None):
        if outline:
            pygame.draw.rect(surface, colors["WEISS"], (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            text = TButton.font.render(self.text, True, colors["TURKIS"])
            surface.blit(text, (self.x + (self.width // 2 - text.get_width() // 2),
                                self.y + (self.height // 2 - text.get_height() // 2)))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False
