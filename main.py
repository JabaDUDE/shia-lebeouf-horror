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

# function to display choices
def choices(choices):
    for num, option in choices.items():
        print("{} : {}".format(num, option))


clear()
answer = input(f'Ready you ready to try and survive the mighty {killer.name}?! (y/n) ')

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

choices(choice_one)

print('----------------------------------------------------------------')

answer_one = None

while answer_one not in choice_one.keys():
    answer_one = input("What do you do?: ")

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
print("As you're running for your life from {}, you start wondering why he's doing out here in the woods, why he seems to be killing for fun, and why there seems to be human flesh stuck between his teeth. Was {} an actual cannibal?".format(killer.name, killer.name))

sleep(15)
clear()

print("After running for what seems like forever, you stop when you notice that he's no longer behind you. It's dark but you seem to have lost him.")
print("But you're hopelessly lost yourself. Afraid that he may be nearby still, you silently creep through the underbrush.")
print("After a few minutes of walking, you spot a small cottage with a light on inside.")
print("You heave a sigh of relief and start to hope that this nightmare will soon be over. You start to walk towards the cottage.")

sleep(10)
clear()

print("Suddenly, you feel a sharp pain in your right leg! You look down and notice that you have your foot stuck in a bear trap!")

choice_two = {
    'a': 'scream as loudly as possible',
    'b': 'call out for help',
    'c': 'gnaw off your leg',
    'd': 'try to remove the bear trap'
}

count = 0

choices(choice_two)

print('----------------------------------------------------------------')

answer_two = None

while answer_two not in choice_two.keys():
    answer_two = input("What do you do?: ")

# What happens if user inputs 'n' before the count reaches 3? TODO: fix bug where if user hits 'n' and then answers question about what choice they want to try next, it doesn't display anything.
if answer_two == 'd':
    ans = 'y'
    while ans == 'y' and count < 3:
        clear()
        ans = input("It doesn't work. Do you want to try again? (y/n): ")
        count += 1
        if ans == 'n':
            choices(choice_two)
            answer_two = None

    if ans == 'y' and count == 3:
        print("You took too long and bled out!")
        print("Game over!")
        exit()
    while answer_two not in choice_two.keys():
        answer_two = input("What do you do?: ")
elif answer_two == 'b':
    print("{} comes skipping merrily out of the cottage and comes straight for you. You're not sure what's scarier: death or having your last sight be of a grown man drenched in blood skipping happily through a field of floweres.".format(killer.name))
    print("Game over!")
    exit()
elif answer_two == 'a':
    print("As you curse every God you can think of and the person that planted this trap, you fail to notice {} come running out of the cottage. You may be dead but screaming was actually kind of a nice stress reliever.".format(killer.name))
    print("Game over!")
    exit()

