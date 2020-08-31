from classes.game import Bcolors, Person
from classes.magic import Spell
from classes.inventory import Item


# Create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 120, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Earthquake", 14, 140, "black")

# Create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hi_potion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
super_potion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
exilir = Item("Elixir", "elixir", "Fully resores HP/MP of one party member", 9999)
hi_exilir = Item("MegaElixir",  "elixir", "Fully restores HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

# list of magic and items
player_magic = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{"item": potion, "quantity": 5},
                {"item": hi_potion, "quantity": 5},
                {"item": super_potion, "quantity": 5},
                {"item": exilir, "quantity": 5},
                {"item": hi_exilir, "quantity": 5},
                {"item": grenade, "quantity": 5}]

enemy_magic = [fire, thunder, blizzard, meteor]
enemy_items = [potion, hi_potion, super_potion, exilir, hi_exilir, grenade]


player1 = Person("Valos", 3240, 65, 60, 34, player_magic, player_items)
player2 = Person("Nick ", 2350, 65, 60, 34, player_magic, player_items)
player3 = Person("Robot", 4008, 65, 60, 34, player_magic, player_items)
enemy = Person("Magus", 1200, 65, 60, 23, enemy_magic, enemy_items)

players = [player1, player2, player3]

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "The enemy Attacks!" + Bcolors.ENDC)

while running:
    print("===============================")
    print(Bcolors.BOLD + "Name               HP                                   MP" + Bcolors.ENDC)
    for player in players:
        player.get_stats()

    print("\n")

    for player in players:

        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "points of damage")
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
                enemy.take_damage(magic_dmg)
                print(Bcolors.OKBLUE + "\n" + spell.name + " deals ", str(magic_dmg),
                      "Points of damage" + Bcolors.ENDC + "\n")

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
                player.hp = player1.maxhp
                player.mp = player1.maxmp
                print(Bcolors.OKGREEN + "\n" + item.name, "Fully restores HP/MP" + Bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.props)
                print(Bcolors.FAIL + "\n" + item.name, "deals", str(item.props), "points of damage" + Bcolors.ENDC)

    enemy_choice = 1

    enemy_damage = enemy.generate_damage()
    player1.take_damage(enemy_damage)
    print("Enemy attacks for", enemy_damage)

    print("-------------------------------")
    print("Enemy HP", Bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + Bcolors.ENDC + "\n")

    print("\n")

    if enemy.get_hp() == 0:
        print("////////////////////////////////////////////////")
        print("\n" + Bcolors.OKGREEN + "YOU WIN!!" + Bcolors.ENDC)
        running = False
    elif player1.get_hp() == 0:
        print("////////////////////////////////////////////////")
        print("\n" + Bcolors.FAIL + "Enemy has defeated you!" + Bcolors.ENDC)
        running = False
