from classes.game import Bcolors, Person


magic = [{'name': 'Fire', 'cost':10, 'dmg': 100},
         {'name': 'Thunderbolt', 'cost':10, 'dmg': 120},
         {'name': 'Blizzard', 'cost':10, 'dmg': 100}]

player1 = Person(400, 65, 60, 34, magic)
enemy = Person(1200, 65, 60, 23, magic)

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
        print("You attacked for", dmg, "points of dammage")
    elif index == 1:
        player1.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1
        magic_dmg = player1.generate_spell_damage(magic_choice)
        spell = player1.get_spell_name(magic_choice)
        cost = player1.get_spell_mp_cost(magic_choice)

        current_mp = player1.get_mp()

        if cost > current_mp:
            print(Bcolors.FAIL + "\n not enough mp \n" + Bcolors.ENDC)
            continue

        player1.reduce_mp(cost)
        enemy.take_damage(magic_dmg)

        print(Bcolors.OKBLUE + "\n" + spell + " deals ", str(magic_dmg), "Ponts of damage" + Bcolors.ENDC + "\n")


    enemy_choice = 1

    enemy_damage = enemy.generate_damage()
    player1.take_damage(enemy_damage)
    print("Enemy attacks for", enemy_damage)

    print("-------------------------------")
    print("Enemy HP", Bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + Bcolors.ENDC + "\n")
    print("Your HP", Bcolors.OKGREEN + str(player1.get_hp()) + "/" + str(player1.get_max_hp()) + Bcolors.ENDC)
    print("Your MP", Bcolors.OKBLUE + str(player1.get_mp())+ "/" + str(player1.get_max_mp()) + Bcolors.ENDC)


    if enemy.get_hp() == 0:
        print(Bcolors.OKGREEN + "You win!!" + Bcolors.ENDC)
    elif player1.get_hp() == 0:
        print(Bcolors.FAIL + "Enemy has defeated you!" + Bcolors.ENDC)
