# This is a sample Python script.

from time import sleep
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# A horror pick your own adventure to run from or beat Shia LeBeouf (based on the song)
class Killer:
    def __init__(self):
        self.name = 'Shia LeBeouf'
        self.health = 100

    def damage(self, name, dmg):
        attribute = getattr(self, name)
        attribute -= dmg
        setattr(self, name, attribute)


# initiate class. able to affect Shia LeBeouf's health this way'
killer = Killer()


clear()
answer = input(f'Ready you ready to try and survive the mighty {killer.name}?! y/n ')

if answer != 'y':
    exit()

print('Then lets get started! Imagine this: ')
print("You're walking in the woods. There's no one around and your phone is dead.")
print("As you're walking, you notice movement out of the corner of your eye. It's {}.".format(killer.name))

sleep(10)
clear()

print("He's following you, about 30 feet back. He gets down on all fours and breaks into a sprint!")
print("He's gaining on you! {}!".format(killer.name))

sleep(7)
clear()

choice_one = {
    'a': 'run',
    'b': 'fight',
    'c': "stare at him and try to intimidate him",
    'd': "stand really still and hope he doesn't see you"
}

for num, option in choice_one.items():
    print("{} : {}".format(num, option))

print('----------------------------------------------------------------')

answer_one = None

while answer_one not in choice_one.keys():
    answer_one = input("What do you do? ")

clear()
print("You decided to {}".format(choice_one[answer_one]))

if answer_one == 'b':
    print("You turn to face him and as he approaches you swing a fist at him.")
    print("However, he does a full sprint kick into your head and knocks you to the ground")
    print("As you try to gain your bearings, he kills and eats you.")
    print("Game Over!")
    exit()
elif answer_one == 'c':
    print("It doesn't work at all and he does a flying kick to your face. Then kills and eats you.")
    print("Game Over!")
    exit()
elif answer_one == 'd':
    print("There are no human shaped trees in your surroundings so you don't blend in that well. He definitely saw you.")
    print("He does a full sprint flying kick to your face. Then kills and eats you while you're on the ground trying to gain your bearings.")
    exit()

print("You break into a sprint and search for your car but you're all turned around.")
print("He's almost upon you now and you see his face is covered in blood. My God, there's blood everywhere!")
print("You give up looking for your car and just focus on outrunning Hollywood superstar {}, who just brandished a knife behind you.".format(killer.name))
