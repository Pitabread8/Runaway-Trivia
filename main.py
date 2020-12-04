from menu import Menu
from logic import Player
from lists import rules
from lists import responses
from lists import credits
# from dicts import continents
from dicts import easy
from dicts import medium
from dicts import hard
from dicts import medium_bonus
from dicts import hard_bonus
import time
import random


# Prints rules
def Rules():
    for i in rules:
        print(i)
        time.sleep(2)


# Prints credits
def Credits():
    for l in credits:
        time.sleep(2)
        print(f"{l:^50}")


# Creates player object
Player = Player(3)

# Creates starting menus
begin = Menu(["Instructions", "Play"])
difficulty = Menu(["Easy", "Medium", "Hard"])
print("Welcome to Runaway Trivia!")
begin.display()
selection = eval(input("Enter Choice Here: "))

# Prints rules/starts game
if selection == 0:
    Rules()
print("Pick your difficulty.")
difficulty.display()
challenge = eval(input("Enter Choice Here: "))

# Location list
continents = {"easy": ["Asia", "Europe"], "medium": ["Asia", "Europe", "North America"],
              "hard": ["Asia", "Europe", "North America", "South America", "Africa"]
              }

# Creates menus for choosing destinations
easy_picker = Menu(continents["easy"])
medium_picker = Menu(continents["medium"])
hard_picker = Menu(continents["hard"])


# Creates list of question indices to choose from
def qdict(p1, p2):
    for c in range(len(p1)):
        p2[c] = []
        for q in range(len(list(p1[c].keys()))):
            p2[c].append(q)


# Choose destination
def destination(p1):
    print("\nPick your location.")
    p1.display()
    place = eval(input("Enter Choice Here: "))
    return place


# Ask question and check answer
def check(p1, p2, p3, p4):
    a = input(f"{p1} ").lower()
    if a != p2[p1].lower():
        Player.lives -= 1
        print(random.choice(p3[1]))
        Player.getInfo()
    else:
        print(random.choice(p3[0]))
    p4.remove(question)


# If a location runs out
def placecheck(p1, p2, p3, p4, p5):
    if len(p1[p2]) == 0 and len(p3) == 1:
        p3.remove(p3[p4])
        del p1[p2]

    elif len(p1[p2]) == 0 and len(p3) > 1:
        print(f"You stayed in {p5} for too long!")
        p3.remove(p3[p4])
        del p1[p2]


# If lives run out - bonus question
def bonusq(p1, p2):
    bonusq = random.choice(p1)
    ans = input(f"{bonusq} ").lower()

    if ans == p2[bonusq].lower():
        Player.lives = 3
        print("Good Job! Your lives have been restored.")
        del p2[bonusq]
        return True


def win(p1):
    endTime = time.time() - startTime
    print(f"\nYou did it! The police have given up. You took {endTime:.1f} seconds and lost {p1} lives.")
    Credits()


startTime = time.time()

if challenge == 0:
    # Creates list of question indices to choose from
    easyqdict = {}
    qdict(easy, easyqdict)

    while True:
        # Choose destination
        place = destination(easy_picker)
        location = continents["easy"][place]
        print(f"\nYou are in {location}.")

        # Select a question from the keys
        keylist = list(easyqdict.keys())  # Creates a list of 0 & 1 for each continent
        key = keylist[place]  # The list of questions in the continent, 0, 1, 2, etc.
        question = random.choice(easyqdict[key])  # Chooses an item from the questions in the continent
        qlist = (list(easy[key].keys()))  # Create a list of questions

        # Ask question and check answer
        check(qlist[question], easy[key], responses, easyqdict[key])

        # If a location runs out
        placecheck(easyqdict, key, continents["easy"], place, location)

        # If lives run out
        if Player.isAlive() == False:
            print("\nYou have lost all of your lives. The police caught up with you. Try again!")
            break

        # If questions run out
        if len(continents["easy"]) == 0:
            win(3 - (Player.lives))
            break

if challenge == 1:
    # Creates list of question indices to choose from
    mediumqdict = {}
    qdict(medium, mediumqdict)

    # Counts deaths (loss of 3 lives)
    counter = 0

    while True:
        # Choose destination
        place = destination(medium_picker)
        location = continents["medium"][place]
        print(f"\nYou are in {location}.")

        # Select a question from the keys
        keylist = list(mediumqdict.keys())  # Creates a list of 0 & 1 for each continent
        key = keylist[place]  # The list of questions in the continent, 0, 1, 2, etc.
        question = random.choice(mediumqdict[key])  # Chooses an item from the questions in the continent
        qlist = (list(medium[key].keys()))  # Create a list of questions

        # Ask question and check answer
        check(qlist[question], medium[key], responses, mediumqdict[key])

        # If a location runs out
        placecheck(mediumqdict, key, continents["medium"], place, location)

        # Create bonus question list
        new_medium_bonus = medium_bonus

        # If lives run out - bonus question
        if not Player.isAlive() and counter == 0:
            counter += 1
            print("\nYou have lost all of your lives. You get one revival question.")
            if not bonusq(list(new_medium_bonus.keys()), new_medium_bonus):
                print("\nYou have lost all of your lives. The police caught up with you. Try again!")
                break

        # If lives run out
        elif Player.isAlive() == False and counter > 0:
            print("\nYou have lost all of your lives. The police caught up with you. Try again!")
            break

        # If questions run out
        if len(continents["medium"]) == 0:
            win((3 * counter) + (3 - Player.lives))
            break

if challenge == 2:
    # Creates list of question indices to choose from
    hardqdict = {}
    qdict(hard, hardqdict)

    # Counts deaths (loss of 3 lives)
    counter = 0

    while True:
        # Choose destination
        place = destination(hard_picker)
        location = continents["hard"][place]
        print(f"\nYou are in {location}.")

        # Select a question from the keys
        keylist = list(hardqdict.keys())  # Creates a list of 0 & 1 for each continent
        key = keylist[place]  # The list of questions in the continent, 0, 1, 2, etc.
        question = random.choice(hardqdict[key])  # Chooses an item from the questions in the continent
        qlist = (list(hard[key].keys()))  # Create a list of questions

        # Ask question and check answer
        check(qlist[question], hard[key], responses, hardqdict[key])

        # If a location runs out
        placecheck(hardqdict, key, continents["hard"], place, location)

        # Create bonus question list
        new_hard_bonus = hard_bonus

        # If lives run out - bonus question 1
        if not Player.isAlive() and counter <= 1:
            counter += 1
            print("\nYou have lost all of your lives. Here is a revival question.")
            if not bonusq(list(new_hard_bonus.keys()), new_hard_bonus):
                print("\nYou have lost all of your lives. The police caught up with you. Try again!")
                break

        # If lives run out
        elif Player.isAlive() == False and counter > 1:
            print("\nYou have lost all of your lives. The police caught up with you. Try again!")
            break

        # If questions run out
        if len(continents["hard"]) == 0:
            win((3 * counter) + (3 - Player.lives))
            break
