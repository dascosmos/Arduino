import random


class Bcolors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:

    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', 'Items']

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

        return self.hp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def choose_action(self):
        i = 1
        print(Bcolors.BOLD + self.name + Bcolors.ENDC)
        print(Bcolors.OKBLUE + "Actions" + Bcolors.ENDC)
        for item in self.actions:
            print("     ", str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print(Bcolors.OKBLUE + "Magic" + Bcolors.ENDC)
        for spell in self.magic:
            print("     ", str(i) + ":", spell.name, "{cost: ", str(spell.cost) + "}")
            i += 1

    def choose_items(self):
        i = 1
        print(Bcolors.OKBLUE + "Items" + Bcolors.ENDC)
        for item in self.items:
            print("     ", str(i) + ":", item["item"].name, ": ", str(item["item"].description), "(x" +
                  str(item["quantity"]) + ")")
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n" + Bcolors.FAIL + Bcolors.BOLD + "    TARGET:" + Bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("     ", str(i) + ".", enemy.name)
                i += 1
        choice = int(input("    Choose target: ")) - 1
        return choice

    def get_stats(self):

        hp_bars = ""
        hp_bar_thick = (self.hp / self.maxhp) * 100 / 4

        while hp_bar_thick > 0:
            hp_bars += "█"
            hp_bar_thick -= 1

        while len(hp_bars) < 25:
            hp_bars += " "

        mp_bars = ""
        mp_bar_thick = (self.mp / self.maxmp) * 100 / 10

        while mp_bar_thick > 0:
            mp_bars += "█"
            mp_bar_thick -= 1

        while len(mp_bars) < 10:
            mp_bars += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0:
                current_mp += " "
                decreased -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string

        print("                   _________________________              __________")
        print(Bcolors.BOLD + self.name + "    " + current_hp + "|" +
              Bcolors.OKGREEN + hp_bars + Bcolors.ENDC +
              "|     " + Bcolors.BOLD + current_mp + "|" + Bcolors.OKBLUE + mp_bars +
              Bcolors.ENDC + "|")

    def get_enemy_stats(self):

        hp_bars = ""
        hp_bar_thick = (self.hp / self.maxhp) * 100 / 2

        while hp_bar_thick > 0:
            hp_bars += "█"
            hp_bar_thick -= 1

        while len(hp_bars) < 50:
            hp_bars += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        separator = ""
        cont = 0
        while cont < len(self.name + "    " + current_hp + "|"):
            separator += " "
            cont += 1

        separator += "__________________________________________________"
        print(separator)
        print(Bcolors.BOLD + self.name + "    " + current_hp + "|" +
              Bcolors.FAIL + hp_bars + Bcolors.ENDC +
              "|     ")

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        pct = self.hp / self.maxhp * 100
        # TODO: review this implementation
        if self.mp < spell.cost or spell.type == "white" and pct > 50:
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg
