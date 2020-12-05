from menu import Menu
from logic import Player, Logic
from lists import modes, responses
from dicts import continents, easy, medium, hard, medium_bonus, hard_bonus
import time
import random

# Creates player object
Player = Player(3)
User = Logic("Player")

# Creates and prints starting menu
begin = Menu(["Instructions", "Play"])
User.Type("Welcome to Runaway Trivia!")
begin.display()
selection = eval(input("Enter Choice Here: "))
if selection == 0:
    User.Rules()

# Creates/prints mode menu
difficulty = Menu(["Easy", "Medium", "Hard"])
print("Pick your difficulty.")
difficulty.display()
challenge = eval(input("Enter Choice Here: "))
mode_str = f"You selected {modes[challenge]} mode."
User.Type(mode_str)

# Creates menus for choosing destinations
easy_picker = Menu(continents["easy"])
medium_picker = Menu(continents["medium"])
hard_picker = Menu(continents["hard"])

def check2(p1):
    if User.check(question, key, p1) == False:
            Player.lives -= 1
            User.Type(random.choice(responses[1]))
            Player.getInfo()
    else:
        User.Type(random.choice(responses[0]))

# Global variables
startTime = time.time()
continents2 = continents

if challenge == 0:
    # Creates list of question indices to choose from
    easyq = easy

    while True:
        # Choose destination
        place = User.destination(easy_picker)
        location = continents["easy"][place]
        location_str = f"\nYou are in {location}."
        User.Type(location_str)

        # Select a question from the keys
        key = easyq[place]  # The list of questions in the continent, 0, 1, 2, etc.
        qlist = (list(key.keys()))  # Create a list of questions
        question = random.choice(qlist)  # Chooses an item from the questions in the continent

        # Ask question and check answer
        check2(easyq[place])

        # If a location runs out
        User.placecheck(location, continents2["easy"], easyq, place, easy)

        # If lives run out
        if Player.isAlive() == False:
            User.lose()
            break

        # If questions run out
        if len(continents["easy"]) == 0:
            endTime = time.time() - startTime
            User.win(endTime, 3 - (Player.lives))
            break

if challenge == 1:
    # Creates list of question indices to choose from
    mediumq = medium

    # Counts deaths (loss of 3 lives)
    counter = 0

    while True:
        # Choose destination
        place = User.destination(medium_picker)
        location = continents["medium"][place]
        location_str = f"\nYou are in {location}."
        User.Type(location_str)

        # Select a question from the keys
        key = mediumq[place]  # The list of questions in the continent, 0, 1, 2, etc.
        qlist = (list(key.keys()))  # Create a list of questions
        question = random.choice(qlist)  # Chooses an item from the questions in the continent

        # Ask question and check answer
        check2(mediumq[place])

        # If a location runs out
        User.placecheck(location, continents2["medium"], mediumq, place, medium)

        # Create bonus question list
        new_medium_bonus = medium_bonus

        # If lives run out - bonus question
        if not Player.isAlive() and counter == 0:
            counter += 1
            print("\nYou have lost all of your lives. You get one revival question.")
            if not User.bonusq(list(new_medium_bonus.keys()), new_medium_bonus):
                User.lose()
                break

        # If lives run out
        elif Player.isAlive() == False:
            User.lose()
            break

        # If questions run out
        if len(continents["medium"]) == 0:
            endTime = time.time() - startTime
            User.win(endTime, (3 * counter) + (3 - Player.lives))
            break

if challenge == 2:
    # Creates list of question indices to choose from
    hardq = hard

    # Counts deaths (loss of 3 lives)
    counter = 0

    while True:
        # Choose destination
        place = User.destination(hard_picker)
        location = continents["hard"][place]
        location_str = f"\nYou are in {location}."
        User.Type(location_str)

        # Select a question from the keys
        key = hardq[place]  # The list of questions in the continent, 0, 1, 2, etc.
        qlist = (list(key.keys()))  # Create a list of questions
        question = random.choice(qlist)  # Chooses an item from the questions in the continent

        # Ask question and check answer
        check2(hardq[place])

        # If a location runs out
        User.placecheck(location, continents2["hard"], hard, place, hard)

        # Create bonus question list
        new_hard_bonus = hard_bonus

        # If lives run out - bonus question 1
        if not Player.isAlive() and counter == 0:
            counter += 1
            print("\nYou have lost all of your lives. Here is a revival question.")
            if not User.bonusq(list(new_hard_bonus.keys()), new_hard_bonus):
                User.lose()
                break

        # If lives run out - bonus question 2
            if not Player.isAlive() and counter == 1:
                print("\nYou have lost all of your lives. Here is a revival question.")
                if not User.bonusq(list(new_hard_bonus.keys()), new_hard_bonus):
                    User.lose()
                    break

        # If lives run out
        elif Player.isAlive() == False:
            User.lose()
            break

        # If questions run out
        if len(continents["hard"]) == 0:
            endTime = time.time() - startTime
            User.win(endTime, (3 * counter) + (3 - Player.lives))
            break
        