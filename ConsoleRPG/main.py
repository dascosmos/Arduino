from classes.game import Bcolors, Person
from classes.magic import Spell
from classes.inventory import Item
import random


# Create black magic
fire = Spell("Fire", 10, 600, "black")
thunder = Spell("Thunder", 10, 600, "black")
blizzard = Spell("Blizzard", 10, 600, "black")
meteor = Spell("Meteor", 20, 1200, "black")
quake = Spell("Earthquake", 14, 600, "black")

# Create white magic
cure = Spell("Cure", 12, 600, "white")
cura = Spell("Cura", 25, 1500, "white")
curaga = Spell("Curaga", 50, 6000, "white")

# create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hi_potion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
super_potion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully resores HP/MP of one party member", 9999)
hi_elixir = Item("MegaElixir",  "elixir", "Fully restores HP/MP of all party members", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

# list of magic and items
player_magic = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 5},
                {"item": hi_potion, "quantity": 5},
                {"item": super_potion, "quantity": 5},
                {"item": elixir, "quantity": 5},
                {"item": hi_elixir, "quantity": 5},
                {"item": grenade, "quantity": 5}]

enemy_magic = [fire, curaga]
enemy_items = [potion, hi_potion, super_potion, elixir, hi_elixir, grenade]


player1 = Person("Valos", 3240, 125, 200, 310, player_magic, player_items)
player2 = Person("Nick ", 2350, 150, 350, 250, player_magic, player_items)
player3 = Person("Robot", 4008, 210, 150, 275, player_magic, player_items)

enemy1 = Person("Imp", 1050, 200, 500, 300, enemy_magic, enemy_items)
enemy2 = Person("Magus", 11200, 300, 700, 350, enemy_magic, enemy_items)
enemy3 = Person("Imp", 1050, 200, 500, 300, enemy_magic, enemy_items)

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "The enemy Attacks!" + Bcolors.ENDC)

while running:
    print("===============================")
    print(Bcolors.BOLD + "Name               HP                                   MP" + Bcolors.ENDC)
    for player in players:
        player.get_stats()

    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    print("\n")

    for player in players:

        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + " has died.")
                del enemies[enemy]

            print("You attacked", enemies[enemy].name, "for", dmg, "points of damage")
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(Bcolors.FAIL + "\n not enough mp \n" + Bcolors.ENDC)
                continue

            if spell.type == "white":
                player.heal(magic_dmg)
                print(Bcolors.OKBLUE + "\n" + spell.name, "heals for", str(magic_dmg) + Bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(Bcolors.OKBLUE + "\n" + spell.name + " deals ", str(magic_dmg),
                      "Points of damage to", enemies[enemy].name + Bcolors.ENDC + "\n")
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died.")
                    del enemies[enemy]
            player.reduce_mp(spell.cost)

        elif index == 2:
            player.choose_items()
            item_choice = int(input("Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(Bcolors.FAIL + "\n" + "None left..." + Bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.props)
                print(Bcolors.OKGREEN + "\n" + item.name, "Heals for", str(item.props) + Bcolors.ENDC)
            elif item.type == "elixir":
                if item.name == "MegaElixir":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player1.maxhp
                    player.mp = player1.maxmp
                print(Bcolors.OKGREEN + "\n" + item.name, "Fully restores HP/MP" + Bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.props)
                print(Bcolors.FAIL + "\n" + item.name, "deals", str(item.props), "points of damage to",
                      enemies[enemy].name + Bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died.")
                    del enemies[enemy]

    print("\n")
    # Check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1
    # check if enemies are defeated
    if defeated_enemies == 3:
        print("////////////////////////////////////////////////")
        print("\n" + Bcolors.OKGREEN + "YOU WIN!!" + Bcolors.ENDC)
        running = False
    # check if players are defeated
    elif defeated_players == 3:
        print("////////////////////////////////////////////////")
        print("\n" + Bcolors.FAIL + "Enemy has defeated you!" + Bcolors.ENDC)
        running = False

    print("\n")
    # Enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)
        if enemy_choice == 0:
            target = random.randrange(0, 3)
            enemy_damage = enemy.generate_damage()
            players[target].take_damage(enemy_damage)

            print(enemy.name, "attacks", players[target].name, "for", enemy_damage)
        elif enemy_choice == 1:
            magic_choice = random.randrange(0, len(enemy.magic))
            spell = enemy.magic[magic_choice]
            if enemy.get_mp() < spell.cost:
                continue

            magic_dmg = spell.generate_damage()

            if spell.type == "white":
                if enemy.get_hp() / enemy.get_max_hp() * 100 < 50:
                    enemy.heal(magic_dmg)
                    print(Bcolors.OKBLUE + spell.name, "heals for", str(magic_dmg) + Bcolors.ENDC)
                    enemy.reduce_mp(spell.cost)
                else:
                    continue
            elif spell.type == "black":
                target = random.randrange(0, 3)
                players[target].take_damage(magic_dmg)
                print(Bcolors.OKBLUE + "\n" + enemy.name + "'s" + spell.name + " deals ", str(magic_dmg),
                      "Points of damage to", players[target].name + Bcolors.ENDC + "\n")
                if players[target].get_hp() == 0:
                    print(players[target].name + " has died.")
                    del players[target]
                enemy.reduce_mp(spell.cost)
