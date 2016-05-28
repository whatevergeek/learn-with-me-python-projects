import random

class Monster:
    def __init__(self, name):
        self.health = 100
        self.name = name
    def punch(self):
        self.health -= random.randrange(18,26)
        if (self.health < 0):
            self.health = 0
        print("%s was punched." % self.name)
    def fart(self):
        self.health -= random.randrange(10,36)
        if (self.health < 0):
            self.health = 0
        print("%s was farted upon." % self.name)
    def heal(self):
        if (self.health <= 35):
            self.health += random.randrange(18,26)
        else:
            self.health += random.randrange(24,26)
        if (self.health > 100):
            self.health = 100
        print("%s received some healing." % self.name)

player = Monster("Player")
computer = Monster("Computer")
print("Player Health: %d" % player.health )
print("Computer Health: %d" % computer.health )
print("")

while(player.health > 0 and computer.health > 0):
    print("Select your move:")
    print("1 - Punch (Damage = 18-25%)")
    print("2 - Fart (Damage = 10-35%)")
    print("3 - Heal")
    choice = int(raw_input("Number of move: "))

    if (choice == 1):
        computer.punch()
    elif (choice == 2):
        computer.fart()
    elif (choice == 3):
        player.heal()
    else:
        print("Invalid choice.")
        continue

    computer_choice = random.randrange(1,4)
    if (computer_choice == 1):
        player.punch()
    elif (computer_choice == 2):
        player.fart()
    elif (computer_choice == 3):
        computer.heal()
    
    print("")
    print("Player Health: %d" % player.health )
    print("Computer Health: %d" % computer.health )
    print("")
    




