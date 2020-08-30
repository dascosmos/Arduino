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
exilir = Item("Exilir", "exilir", "Fully resores HP/MP of one party member", 9999)
hi_exilir = Item("MegaExilir",  "exilir", "Fully restores HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

# list of magic and items
player_magic = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [potion, hi_potion, super_potion, exilir, hi_exilir, grenade]

enemy_magic = [fire, thunder, blizzard, meteor]
enemy_items = [potion, hi_potion, super_potion, exilir, hi_exilir, grenade]


player1 = Person(400, 65, 60, 34, player_magic, player_items)
enemy = Person(1200, 65, 60, 23, enemy_magic, enemy_items)

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "The enemy Attacks!" + Bcolors.ENDC)

while running:
    print("===============================")
    player1.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player1.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage")
    elif index == 1:
        player1.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1

        if magic_choice == -1:
            continue

        spell = player1.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player1.get_mp()

        if spell.cost > current_mp:
            print(Bcolors.FAIL + "\n not enough mp \n" + Bcolors.ENDC)
            continue

        if spell.type == "white":
            player1.heal(magic_dmg)
            print(Bcolors.OKBLUE + "\n" + spell.name, "heals for", str(magic_dmg) + Bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(Bcolors.OKBLUE + "\n" + spell.name + " deals ", str(magic_dmg),
                  "Points of damage" + Bcolors.ENDC + "\n")

        player1.reduce_mp(spell.cost)

    elif index == 2:
        player1.choose_items()
        item_choice = int(input("Choose item: ")) - 1

        if item_choice == -1:
            continue

        item = player1.items[item_choice]

        if item.type == "potion":
            player1.heal(item.props)
            print(Bcolors.OKGREEN + "\n" + item.name, "Heals for", str(item.props) + Bcolors.ENDC)

    enemy_choice = 1

    enemy_damage = enemy.generate_damage()
    player1.take_damage(enemy_damage)
    print("Enemy attacks for", enemy_damage)

    print("-------------------------------")
    print("Enemy HP", Bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + Bcolors.ENDC + "\n")
    print("Your HP", Bcolors.OKGREEN + str(player1.get_hp()) + "/" + str(player1.get_max_hp()) + Bcolors.ENDC)
    print("Your MP", Bcolors.OKBLUE + str(player1.get_mp()) + "/" + str(player1.get_max_mp()) + Bcolors.ENDC)
    print("\n")

    if enemy.get_hp() == 0:
        print("////////////////////////////////////////////////")
        print("\n" + Bcolors.OKGREEN + "YOU WIN!!" + Bcolors.ENDC)
        running = False
    elif player1.get_hp() == 0:
        print("////////////////////////////////////////////////")
        print("\n" + Bcolors.FAIL + "Enemy has defeated you!" + Bcolors.ENDC)
        running = False
