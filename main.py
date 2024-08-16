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
    #     self.health = 100

    # def damage(self, name, dmg):
    #     attribute = getattr(self, name)
    #     attribute -= dmg
    #     setattr(self, name, attribute)


# initiate class. able to affect Shia LeBeouf's health this way'
killer = Killer()

# function to display choices
def choices(choices):
    for num, option in choices.items():
        print("{} : {}".format(num, option))

# TODO: does not properly display text
# function to print out bad options, hopefully allows reusability and fix bug on 135
# def choice_made(choice, options):
#     if choice in options.items():
#         print_items = options[choice]
#         for num, item in print_items:
#             print("{}".format(item))
#             if num == len(print_items):
#                 exit()


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
print("As you're running for your life from {}, you start wondering why he's doing out here in the woods, why he seems to be killing for fun, \nand why there seems to be human flesh stuck between his teeth. Was {} an actual cannibal?".format(killer.name, killer.name))

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


if answer_two == 'd':
    ans = 'y'
    while ans == 'y' and count < 3:
        clear()
        ans = input("It doesn't work. Do you want to try again? (y/n): ")
        count += 1
# What happens if user inputs 'n' before the count reaches 3? TODO: fix bug where if user hits 'n' and then answers question about what choice they want to try next, it doesn't display anything.
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
    print(f"As you curse every God you can think of and the person that planted this trap, you fail to notice {killer.name} come running out of the cottage. You may be dead but screaming was actually kind of a nice stress reliever.")
    print("Game over!")
    exit()

clear()

print("You spend the next hour gnawing off your leg as quietly as possible. Eventually it comes off and you grab a nearby stick to use as a crutch.")
print("You limp towards the cottage, being careful to not make more noise.")
print("As you approach the doorstep, you peer into the window. Your eyes go wide. It's him. It's {}".format(killer.name))
print("He's sitting on a chair, sharpening an axe. He doesn't seem to have noticed you yet.")

sleep(15)
clear()


choice_three = {
    'a' : 'bust down the door and charge in screaming',
    'b' : 'sneak inside and attemp to strangle him',
    'c' : 'try to sneak away'
}

choices(choice_three)

print('----------------------------------------------------------------')

answer_three = None

while answer_three not in choice_three.keys():
    answer_three = input("What do you do?: ")

clear()


# TODO: fix function so it displays text
# options_three = {
#     'a': ["You try to bust down the door but with a stump leg it doesn't really look at cool as it does in the movies.","Especially the part where the as the door opens, you stumble forward and end up on the ground.",f"Needless to say {killer.name} was happy to have his prey come to him.","You died. Game over!"],
#     'c': ["In a panic, you turn and try to quietly make your way down the steps; however, the stick you're using as a crutch slips and you end up falling backwards onto the porch, making a loud sound.","You hear noise inside and footsteps coming towards you. You scramble to get up, but by the time you get on your feet, he's already on the porch behind you.","You died. Game over!"]
# }


# choice_made(answer_three, options_three)


if answer_three == 'a':
    print("You try to bust down the door but with a stump leg it doesn't really look at cool as it does in the movies.")
    print("Especially the part where the as the door opens, you stumble forward and end up on the ground.")
    print("Needless to say {} was happy to have his prey come to him.".format(killer.name))
    print("You died. Game over!")
    exit()
elif answer_three == 'c':
    print("In a panic, you turn and try to quietly make your way down the steps; however, the stick you're using as a crutch slips and you end up falling backwards onto the porch, making a loud sound.")
    print("You hear noise inside and footsteps coming towards you. You scramble to get up, but by the time you get on your feet, he's already on the porch behind you.")
    print("You died. Game over!")
    exit()

print("Carefully, you turn the knob of the door and slowly make your way inside. You sneak up behind him.")

choice_four = {
    'a': 'tickle him',
    'b': 'knock him out with your crutch',
    'c': 'strangle him',
    'd': 'wait for him to turn around and scare him'
}

choices(choice_four)

print('----------------------------------------------------------------')

answer_four = None

while answer_four not in choice_four.keys():
    answer_four = input("What do you do?: ")

clear()

if answer_four == 'a':
    print("{} starts laughing. Turns out he's really ticklish.".format(killer.name))
    print("He starts thrashing around with the axe still in his hand.")
    print("It hits you in the side of the head.")
    print("You died. Game over!")
    exit()
elif answer_four == 'b':
    print("You swing your crutch at his head, but it turns out it's hard to swing hard with only one leg.")
    print("{} jumps up and touches his head. There's a little bit a blood but definitely not enough to knock him out.".format(killer.name))
    print("He axes you. You died. Game Over!")
    exit()
elif answer_four == 'd':
    print("You wait for a few minutes and listen to him humming to himself.")
    print("At one point he recites an acceptance speech for numerous awards, some of which sound made up.")
    print("Eventually, he does turn around and you shout right into his face which causes him to scream and jump.")
    print("You have a good laugh before he axes you. It was totally worth it.")
    print("You died. Game over!")
    exit()

print("You strangle superstar {}. You both fall to the floor and you try to wrestle a knife from {}.".format(killer.name, killer.name))
print("You stab him in his kidney. And he stops moving.")
print("Safe at last from {}".format(killer.name))

sleep(10)
clear()

print("You limp into the dark woods, blood oozing from your stump leg.")
print("You've beaten {}".format(killer.name))

sleep(7)
clear()
print("....")
sleep(2)
clear()
print("Wait...")
sleep(2)
clear()
print("He isn't dead! (Shia Surprise!)")
print("There's a gun to your head and death in his eyes!")
sleep(5)
clear()

choice_five = {
    'a': 'try to confuse him',
    'b': 'dodge the bullet like Neo from The Matrix',
    'c': 'body slam him'
}

choices(choice_five)

print('----------------------------------------------------------------')

answer_five = None

while answer_five not in choice_five.keys():
    answer_five = input("What do you do?: ")

clear()

if answer_five == 'a':
    print("You tell him that if he kills you, he'll never learn the truth.")
    print("What truth? He asks.")
    print("The truth of Ligma.")
    print("He shoots you because he already knows where you're going with it.")
    print("You died. Game over!")
    exit()
elif answer_five == 'b':
    print("Turns out bending backwards with only one leg is really hard.")
    print("The first shot misses, tho, but before you can celebrate he shots you in the head with a second shot.")
    print("You died. Game over!")
    exit()

print("You remember you can do jiu-jitsu.")
print("You body slam superstar {}".format(killer.name))
print("Legendary fight with {}".format(killer.name))
print("Normal Tuesday night for {}".format(killer.name))
print("You try to swing an axe at {}, but blood is draining fast from your stump leg".format(killer.name))

sleep(15)
clear()

print("He's dodging every swipe and parries to the left.")
print("You counter to the right, you catch him in the neck.")
print("You're chopping off his head now.")
print("You have just decapitated {}".format(killer.name))

sleep(10)
clear()

print("His head topples to the floor, expressionless.")
print("You fall to the ground and catch your breath.")
print("You're finally safe from {}".format(killer.name))

sleep(10)
clear()

print(f"YOU HAVE BEATEN {killer.name.capitalize()}. YOU WIN!")
exit()
