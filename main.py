# Zoo class
class zoo:
    # Intialization function
    def __init__(self, name):
        self.name = name
        self.animal_lst = []

    # function to add an animal to the list
    def add_animal(self, added_animal):
        self.animal_lst.append(added_animal)

    # prints out every animal in animal_lst
    def print_animal_names(self):
        print("The animals in the " + self.name + " zoo are:")
        for i in range(0, len(self.animal_lst)):
            iterated_animal = self.animal_lst[i]
            print(" " + iterated_animal.name + " the " + iterated_animal.age + " year old " + iterated_animal.gender +
                  " " + iterated_animal.breed + " " + iterated_animal.species)


# Animal class
class animal:
    # Initialization function
    def __init__(self, name, age, species, breed, gender, domain):
        self.name = name
        self.age = age
        self.species = species
        self.breed = breed
        self.gender = gender
        self.domain = domain


# Some testing i did for inheritance classes, doesn't work great for what I'm doing, but taught myself it
"""
class dog(animal):
    def __init__(self, name, age, species, breed, gender):
        super().__init__(name, age, species, breed, gender)


class cat(animal):
    def __init__(self, name, age, species, breed, gender):
        super().__init__(name, age, species, breed, gender)


test = zoo("test")
doggo = animal("Doggo", 1, "Dog", "Husky", "Male", "Terrestrial")
catto = animal("Catto", 1, "Cat", "Tabby", "Female", "Terrestrial")
test.add_animal(doggo)
test.add_animal(catto)
test.print_animal_names()
"""


# function to ask for user response of yes or no
def yes_or_no(question):
    user_choice = input(question + "Y/N\n").lower()
    affirmatives = ["y", "yes", "yeah", "yeap", "ye", "yea"]
    if user_choice in affirmatives:
        return True
    else:
        return False


# Checks to make sure a value can be converted to int, I realize after that I don't actually need this, but made it
# already so I left it
def check_int(check_value):
    try:
        int(check_value)
        return True
    except ValueError:
        print("Invalid Input")
        return False


# Asks if the user wants to make a zooe
if yes_or_no("Hello, would you like to create a new zoo?"):
    # If yes, creates a zoo, and signifies to start the main loop
    zoo_name = input("Great, what should we name it? \n")
    user_zoo = zoo(zoo_name)
    running = True
else:
    # If no, exits out of the program after a message
    print("Very well, have a good day")
    running = False


# Main loop of the program
while running:
    # Asks what the user wants to do
    action_choice = input("Would you like to \n"
                          " 1: Add an animal to your zoo \n"
                          " 2: Look at your current animals \n"
                          " 3: Rename your zoo\n"
                          " 4: Exit\n")
    if action_choice == "1":
        # Asks the user for all the information for their added animal
        animal_species = input("What is your animal's species\n")
        animal_breed = input("What is your animal's breed\n")
        animal_gender = input("What is your animal's gender\n")
        animal_age = input("What is your animal's age (in years)\n")
        animal_domain = input("Does your animal live on/in land, air, water, or hybrid (type the name of where they "
                              "live (i.e 'land', if they live in multiple, pick one or choose hybrid\n")
        animal_name = input("Finally, what is your animal's name\n")
        # Creates the animal
        user_animal = animal(animal_name, animal_age, animal_species, animal_breed, animal_gender, animal_domain)
        # Adds the animal
        user_zoo.add_animal(user_animal)
    elif action_choice == "2":
        # Prints out the animals currently in the zoo
        user_zoo.print_animal_names()
    elif action_choice == "3":
        # Changes the zoo name then tells the user
        user_zoo.name = input("What would you like your zoo's new name to be?\n")
        print("Alright, your zoo's name is now " + user_zoo.name)
    else:
        # incorrect input or '4' will exit the loop
        running = False

try:
    # If the zoo was made
    user_zoo in globals()
    # will ask if the user wants to see the animals again
    if yes_or_no("That was a great time making a zoo, would you like to see the animals for one last time?"):
        # If yes, prints out the animals
        user_zoo.print_animal_names()
    else:
        # If no, leaves a message
        print("Very well, hope to see you again sometime")
except NameError:
    # If they never made a zoo, just passes to the end
    pass
