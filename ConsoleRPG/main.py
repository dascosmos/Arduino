from classes.game import Bcolors, Person


magic = [{'name': 'Fire', 'cost':10, 'dmg': 60},
         {'name': 'Thunderbolt', 'cost':10, 'dmg': 80},
         {'name': 'Blizzard', 'cost':10, 'dmg': 60}]

player1 = Person(400, 65, 60, 34, magic)
enemy = Person(1200, 65, 60, 23, magic)

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "The enemy Attacks!" + Bcolors.ENDC)

while running:
    print("===============================")
    player1.choose_action()
    choice = input("Choos action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player1.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of dammage, enemy hp:", str(enemy.get_hp()))

        running = False