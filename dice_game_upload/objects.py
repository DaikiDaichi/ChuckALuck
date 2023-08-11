from classes import TKonto, TButton, TLabel, TDice, colors

konto = TKonto(100, "Demo")

buttons = {"chuck_a_luck": {
    "info_button": TButton(colors["WEISS"], (550, 50), 50, 50, "?"),
    "return_button": TButton(colors["WEISS"], (400, 50), 100, 50, "Menu"),
    "throw_button": TButton(colors["WEISS"], (250, 50), 100, 50, "werfen"),
    "button1": TButton(colors["WEISS"], (200, 330), 50, 50, "1"),
    "button2": TButton(colors["WEISS"], (270, 330), 50, 50, "2"),
    "button3": TButton(colors["WEISS"], (340, 330), 50, 50, "3"),
    "button4": TButton(colors["WEISS"], (200, 400), 50, 50, "4"),
    "button5": TButton(colors["WEISS"], (270, 400), 50, 50, "5"),
    "button6": TButton(colors["WEISS"], (340, 400), 50, 50, "6")},

    "lootbox": {
    "return_button": TButton(colors["WEISS"], (400, 50), 100, 50, "Menu"),
    "lootbox_1_button": TButton(colors["WEISS"], (100, 50), 150, 50, "Lootbox_1")
    },

    "__main__": {
    "chuck_a_luck_button": TButton(colors["WEISS"], (100, 50), 170, 50, "Chuck A Luck"),
    "lootbox_button": TButton(colors["WEISS"], (370, 50), 170, 50, "Lootbox")
    }
}

labels = {
    "konto_label": TLabel(f"Kontostand: {konto.getBalance()}", (50, 50)),
    "player_choice_label": TLabel(f"Ihre Glückszahl: {1}", (50, 160))
}

dices = {
    "d1": TDice(),
    "d2": TDice(),
    "d3": TDice()
}
