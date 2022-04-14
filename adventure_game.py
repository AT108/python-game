import time
import random


def print_pause(string, seconds):
    print(string)
    time.sleep(seconds)


def intro():
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.", 3)
    print_pause(f"Rumor has it that a {creature} is somewhere around here, "
                "and has been terrifying the nearby village.", 3)
    print_pause("In front of you is a house.", 2)
    print_pause("To your right is a dark cave.", 2)
    print_pause("In your hand you hold your trusty "
                "(but not very effective) torch.\n", 1)


def house_cave_choice(weapon):
    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave.\n", 1)
    print_pause("What would you like to do?\n", 1)
    choice = input("(Please enter 1 or 2)")
    if choice == '1':
        inhouse_choice(weapon)
    elif choice == '2':
        cave(weapon)
        house_cave_choice(weapon)
    else:
        house_cave_choice(weapon)


def house(weapon):
    print_pause("You approach the door of the house.", 2)
    print_pause("You are about to knock when the door opens "
                f"and out steps a {creature}.", 2)
    print_pause(f"Eep! This is the {creature}'s house!", 2)
    print_pause(f"The {creature} attacks you!", 1)


def cave(weapon):
    print_pause("You peer cautiously into the cave.", 2)
    if 'sword' in weapon:
        print_pause("You've been here before, and gotten all the good "
                    "stuff. It's just an empty cave now.", 2)
        print_pause("You walk back out to the field.\n", 2)
    else:
        print_pause("It turns out to be only a very small cave.", 2)
        print_pause("Your eye catches a glint of metal behind a rock.", 2)
        print_pause("You have found the magical Sword of Ogoroth!", 2)
        print_pause("You discard your silly old torch and take the sword "
                    "with you.", 2)
        print_pause("You walk back out to the field.\n", 2)
        weapon.append('sword')


def fight(weapon):
    print_pause("You do your best...", 2)
    print_pause(f"but your torch is no match for the {creature}.", 2)
    print_pause("You have been defeated!", 2)
    play_again(weapon)


def play_again(weapon):
    another_round = input("Would you like to play again? (y/n) ")
    if another_round == 'y':
        choose_creature()
        intro()
        if 'sword' in weapon:
            weapon.remove('sword')
        house_cave_choice(weapon)
    elif another_round == 'n':
        print_pause("OK, have a great day!", 1)
    else:
        play_again(weapon)


def victory(weapon):
    print_pause(f"As the {creature} moves to attack, you unsheath your "
                "new sword.", 2)
    print_pause("The Sword of Ogoroth shines brightly in your hand as you "
                "brace yourself for the attack.", 1)
    print_pause(f"But the {creature} takes one look at your shiny new toy "
                "and runs away!", 1)
    print_pause(f"You have rid the town of the {creature}. "
                "You are victorious!", 2)


def inhouse_choice(weapon):
    house(weapon)
    fight_run = input("Would you like to (1) fight or (2) run away?")
    if fight_run == '1':
        if 'sword' in weapon:
            victory(weapon)
            play_again(weapon)
        else:
            print_pause("You feel a bit under-prepared for this, "
                        "what with only having a tiny torch.", 1)
            fight(weapon)
    elif fight_run == '2':
        print_pause("You run back into the field. Luckily, you don't "
                    "seem to have been followed.\n", 2)
        house_cave_choice(weapon)
    else:
        print_pause("Sorry, that is not a valid option. Try again!\n", 1)
        house_cave_choice(weapon)


def choose_creature():
    global creature
    creatures = ["magician", "dwarf", "terminator", "villain"]
    creature = random.choice(creatures)
    return creature


def entire_game():
    weapon = []
    choose_creature()
    intro()
    house_cave_choice(weapon)


entire_game()
