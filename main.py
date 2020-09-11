#main.py has all of the gameplay and class instances.

easyquestionslist_asia = [
    "Is India in the northern hemisphere, southern hemisphere, or both?",
    "What is the capital of China?",
    "What is the capital of Japan?",
    "What is the main religion in Jordan?",
    "What is the national language of India?",
    "What is the main religion in Israel?",
    "What is the capital of South Korea?"
]
easyquestionslist_europe = [
"What currency is used in France?",
"What is the capital of Germany?",
"What is the capital of the United Kingdom?"
]

mediumquestionslist_asia = [
    "What currency is used in Indonesia?",
    "What is the biggest river that flows through China?",
    "What is the national animal of China?",
    "What is the currency of Japan?",
    "What is the national language of Myanmar?"
]
mediumquestionslist_europe = [
    "What is the capital of Italy?",
    "What is the capital of Scotland?",
    "How many countries are part of the United Kingdom?"
]    
mediumquestionslist_northamerica = [
    "What is the official language of Belize?",
    "What is the currency of Mexico?"
]

hardquestionslist_northamerica = [
    "What is the currency of the U.S?",
    "What is the national flower of the United States?"
]
hardquestionslist_europe = [
    "What currency is used by Russia?",
    "What is the national animal of Scotland?"
]
hardquestionslist_asia = [
    "How many states are in India?", 
    "How many mountains are in Taiwan?"
]
hardquestionslist_southamerica = [
    "What is the official language of Suriname?",
    "How many time zones are there in Brazil?"
]
hardquestionslist_africa = [
    "What is the capital of Morocco?",
    "What is the national language of Ethiopia?"
]

correctresponselist = [
    "The police got lost at the airport. Good job!",
    "It rained heavily last night, and the police got stuck in some mud. Keep going!",
    "The police lost their tickets and are now stranded at the bus stand. Good job!",
    "Yay! You managed to lose the police in a busy crowd.",
    "You managed to hitch a ride on the last boat in the harbor. Good going!",
    "The police's servers \"accidentally\" shut down. Get as far as you can while they reboot!"
]
incorrectresponselist = [
    "Uh oh! You didn’t cover your tracks well!",
    "Your plane got rescheduled. The police are getting closer.",
    "You slipped on a banana peel and got hurt. You have to be more careful!",
    "Oops, you got distracted by a traveling circus. Look at those funny clowns!",
    "You decided to go sightseeing. Unfortunately, so did the police.",
    "Uh oh. Someone saw you and told the police. Better leave soon!"
]

from logic import Player
from logic import Logic
from menu import Menu
import random
import time

def Credits():
  print("Thanks for playing!")
  gamename = "Runaway Trivia"
  category1 = "Designed and Programmed by:"
  category2 = "Information:"
  person1 = "Nikita Sane"
  person2 = "Sita Vemuri"
  info1 = "First released: June 2020"
  info2 = "Made with: Python"
  print(f"\n{gamename:^50} \n")
  print(f"{category1:^50}")
  print(f"{person1:^50}")
  print(f"{person2:^50} \n")
  print(f"{category2:^50}")
  print(f"{info1:^50}")
  print(f"{info2:^50}")

continents_easy = ["Asia", "Europe"]
destinationpicker_easy = Menu(continents_easy)

continents_medium = ["Asia", "Europe", "North America"]
destinationpicker_medium = Menu(continents_medium)

continents_hard = ["Asia", "Europe", "North America", "South America", "Africa"]
destinationpicker_hard = Menu(continents_hard)

Player = Player(3)

#class instances/list
begin = Menu(["Instructions", "Play"])
difficulty = Menu(["Easy", "Medium", "Hard"])

def responsePicker_correct():
  n = random.randint(0, len(correctresponselist) - 1)
  print(correctresponselist[n])

def responsePicker_incorrect():
  n = random.randint(0, len(incorrectresponselist) - 1)
  print(incorrectresponselist[n])

#beginning Menu
print("Welcome to Runaway Trivia!")
begin.display()
selection = eval(input("Enter Choice Here: "))
if selection == 0:
	print(
	    "-This is a game where you, the criminal, move between different locations around the world while running away from the police.\n-You will begin in a random location. From there,you can choose a continent to go to and answer a question about it. Make sure you know some stuff about that location!\n-If you stay in a continent for too long, you will automatically move to a different one and answer a question about the new continent.\n-You can pick easy, medium, or hard questions to answer.\n-To get farther away from the police you must answer the trivia questions quickly and accurately. \n-You have three lives, and you can lose them by getting a question wrong. If you lose all three, you get a bonus question to revive your three lives. If you answer correctly, keep going. However, if you answer incorrectly, the police will catch you and you lose. Game over.\n-The way to win the game is to make it to the end without dying at all in Easy mode, without dying twice in Medium mode, and without dying thrice in Hard mode. \nGood Luck!"
	)
	difficulty.display()
	challenge = eval(input("Enter Choice Here: "))
else:
	print("Pick your difficulty.")
	difficulty.display()
	challenge = eval(input("Enter Choice Here: "))

startTime_easy = time.time()
if challenge == 0:
  print("Pick your location.")
  destinationpicker_easy.display()
  place = eval(input("Enter Choice Here: "))
  location = continents_easy[place]
  print(f"\nYou are in {location}.")

  while True:
    if location == "Asia":
      question = easyquestionslist_asia[random.randint(0, len(easyquestionslist_asia) - 1)]
      easyquestionslist_asia.remove(question)   

      a = input(f"{question} ").lower()
      q = Logic(a)
      if q.EasyIsCorrect_asia(question) == False:
        Player.lives -= 1
        responsePicker_incorrect()
        Player.getInfo()
      else:
        responsePicker_correct()

    if location == "Europe":
      question = easyquestionslist_europe[random.randint(0, len(easyquestionslist_europe) - 1)]
      easyquestionslist_europe.remove(question)  

      a = input(f"{question} ").lower()
      q = Logic(a)
      if q.EasyIsCorrect_europe(question) == False:
        Player.lives -= 1
        responsePicker_incorrect()
        Player.getInfo()
      else:
        responsePicker_correct()

    #If Asia runs out
    if len(easyquestionslist_asia) == 0 and "Asia" in continents_easy:
      print("You stayed in Asia for too long!")
      continents_easy.remove("Asia")

    #If Europe runs out
    if len(easyquestionslist_europe) == 0 and "Europe" in continents_easy:
      print("You stayed in Europe for too long!")
      continents_easy.remove("Europe")
 
    #If lives run out
    if Player.lives == 0:
      print("\nYou have lost all of your lives. The police caught up with you. Try again!")
      break
    
    #If questions run out
    if len(continents_easy) == 0:
      endTime_easy = time.time() - startTime_easy
      print(f"\nYou did it! The police have given up. It took you {endTime_easy: .1f} seconds to finish.")
      Credits()
      break

    print("\nPick your next location.")
    destinationpicker_easy.display()
    place = eval(input("Enter Choice Here: "))
    location = continents_easy[place]
    print(f"\nYou are in {location}.")

startTime_medium = time.time()
if challenge == 1:
  print("Pick your location.")
  destinationpicker_medium.display()
  place = eval(input("Enter Choice Here: "))
  location = continents_medium[place]
  print(f"\nYou are in {location}.")
  
  counter = 0

  while True:
    if location == "Asia":
      question = mediumquestionslist_asia[random.randint(0, len(mediumquestionslist_asia) - 1)]
      mediumquestionslist_asia.remove(question)    
      a = input(f"{question} ").lower()
      q = Logic(a)
      if q.MediumIsCorrect_asia(question) == False:
        Player.lives -= 1
        responsePicker_incorrect()
        Player.getInfo()
      else:
        responsePicker_correct()

    if location == "Europe":
      question = mediumquestionslist_europe[random.randint(0, len(mediumquestionslist_europe) - 1)]
      mediumquestionslist_europe.remove(question)

      a = input(f"{question} ").lower()
      q = Logic(a)
      if q.MediumIsCorrect_europe(question) == False:
        Player.lives -= 1
        responsePicker_incorrect()
        Player.getInfo()
      else:
        responsePicker_correct()

    if location == "North America":
      question = mediumquestionslist_northamerica[random.randint(0, len(mediumquestionslist_northamerica) - 1)]
      mediumquestionslist_northamerica.remove(question)

      a = input(f"{question} ").lower()
      q = Logic(a)
      if q.MediumIsCorrect_northamerica(question) == False:
        Player.lives -= 1
        responsePicker_incorrect()
        Player.getInfo()
      else:
        responsePicker_correct()

    #If Asia runs out
    if len(mediumquestionslist_asia) == 0 and "Asia" in continents_medium:
      print("You stayed in Asia for too long!")
      continents_medium.remove("Asia")

    #If Europe runs out
    if len(mediumquestionslist_europe) == 0 and "Europe" in continents_medium:
      print("You stayed in Europe for too long!")
      continents_medium.remove("Europe")

    #If North America runs out
    if len(mediumquestionslist_northamerica) == 0 and "North America" in continents_medium:
      print("You stayed in North America for too long!")
      continents_medium.remove("North America")

    #If lives run out 
    if Player.lives <= 0 and counter == 0:
      print("\nYou have lost all of your lives. Here is a second chance bonus question (which you only get one of).")
      counter += 1
      a = input("Which continent has the second biggest population? ").lower()
      answer = "Africa"

      if a == answer.lower(): 
        Player.lives = 3
        print("Good Job! Your lives have been restored. ")
      else:
        print("\nYou have lost all of your lives. The police caught up with you. Try again!")
        break
    if Player.lives <= 0 and counter > 0:   
      print("\nYou have lost all of your lives. The police caught up with you. Try again!")
      break

    #If questions run out
    if len(mediumquestionslist_asia) == 0 and len(mediumquestionslist_europe) == 0 and len(mediumquestionslist_northamerica) == 0:
      endTime_medium = time.time() - startTime_medium
      print(f"\nThe police have given up. You win! It took you {endTime_medium: .1f} seconds to finish.")
      Credits()
      break

    print("\nPick your next location.")
    destinationpicker_medium.display()
    place = eval(input("Enter Choice Here: "))
    location = continents_medium[place]
    print(f"\nYou are in {location}.")  	

startTime_hard = time.time()
if challenge == 2:
  print("Pick your location.")
  destinationpicker_hard.display()
  place = eval(input("Enter Choice Here: "))
  location = continents_hard[place]
  print(f"\nYou are in {location}.")
  
  counter = 0

  while True:
    if location == "Asia":
      question = hardquestionslist_asia[random.randint(0, len(hardquestionslist_asia) - 1)]
      hardquestionslist_asia.remove(question)    
      a = input(f"{question} ").lower()
      q = Logic(a)
      if q.HardIsCorrect_asia(question) == False:
        Player.lives -= 1
        responsePicker_incorrect()
        Player.getInfo()
      else:
        responsePicker_correct()

    if location == "Europe":
      question = hardquestionslist_europe[random.randint(0, len(hardquestionslist_europe) - 1)]
      hardquestionslist_europe.remove(question)

      a = input(f"{question} ").lower()
      q = Logic(a)
      if q.HardIsCorrect_europe(question) == False:
        Player.lives -= 1
        responsePicker_incorrect()
        Player.getInfo()
      else:
        responsePicker_correct()

    if location == "North America":
      question = hardquestionslist_northamerica[random.randint(0, len(hardquestionslist_northamerica) - 1)]
      hardquestionslist_northamerica.remove(question)

      a = input(f"{question} ").lower()
      q = Logic(a)
      if q.HardIsCorrect_northamerica(question) == False:
        Player.lives -= 1
        responsePicker_incorrect()
        Player.getInfo()
      else:
        responsePicker_correct()

    if location == "South America":
      question = hardquestionslist_southamerica[random.randint(0, len(hardquestionslist_southamerica) - 1)]
      hardquestionslist_southamerica.remove(question)

      a = input(f"{question} ").lower()
      q = Logic(a)
      if q.HardIsCorrect_southamerica(question) == False:
        Player.lives -= 1
        responsePicker_incorrect()
        Player.getInfo()
      else:
        responsePicker_correct()

    if location == "Africa":
      question = hardquestionslist_africa[random.randint(0, len(hardquestionslist_africa) - 1)]
      hardquestionslist_africa.remove(question)

      a = input(f"{question} ").lower()
      q = Logic(a)
      if q.HardIsCorrect_africa(question) == False:
        Player.lives -= 1
        responsePicker_incorrect()
        Player.getInfo()
      else:
        responsePicker_correct()

    #If Asia runs out
    if len(hardquestionslist_asia) == 0 and "Asia" in continents_hard:
      print("You stayed in Asia for too long!")
      continents_hard.remove("Asia")

    #If Europe runs out
    if len(hardquestionslist_europe) == 0 and "Europe" in continents_hard:
      print("You stayed in Europe for too long!")
      continents_hard.remove("Europe")

    #If North America runs out
    if len(hardquestionslist_northamerica) == 0 and "North America" in continents_hard:
      print("You stayed in North America for too long!")
      continents_hard.remove("North America")
      
    #If South America runs out
    if len(hardquestionslist_southamerica) == 0 and "South America" in continents_hard:
      print("You stayed in South America for too long!")
      continents_hard.remove("South America")

    #If Africa runs out
    if len(hardquestionslist_africa) == 0 and "Africa" in continents_hard:
      print("You stayed in Africa for too long!")
      continents_hard.remove("Africa")

    #If lives run out 
    if Player.lives <= 0 and counter == 0:
      print("\nYou have lost all of your lives. Here is your final bonus question.")
      counter += 1
      a = input("What is the largest desert in the world? ").lower()
      answer = "Antarctica"

      if a == answer.lower(): 
        Player.lives = 3
        print("Good Job! Your lives have been restored. ")
    if Player.lives <= 0 and counter == 1:
      print("\nYou have lost all of your lives. Here is a last bonus question.")
      a = input("Which has more countries: North America or South America? ").lower()
      answer = "North America"

      if a == answer.lower(): 
        Player.lives = 3
        print("Good Job! Your lives have been restored. ")
      else:
        print("\nYou have lost all of your lives. The police caught up with you. Try again!")
        break
        
    if Player.lives <= 0 and counter > 1:  
      print("\nYou have lost all of your lives. The police caught up with you. Try again!")
      break
    
    #If questions run out
    if len(continents_hard) == 0:
      endTime_hard = time.time() - startTime_hard
      print(f"\nThe police have given up. You win! It took you {endTime_hard: .1f} seconds to finish.")
      Credits()
      break
  
    print("\nPick your next location.")
    destinationpicker_hard.display()
    place = eval(input("Enter Choice Here: "))
    location = continents_hard[place]
    print(f"\nYou are in {location}.")  	