from lists import rules, credits
import random
import time
import sys

class Player():
  def __init__(self, lives = 3):
    self.lives = lives
  
  def isAlive(self):
    return self.lives > 0

  def getInfo(self):
    print(f"You have {self.lives} lives left.")

class Logic():
  def __init__(self, name):
    self.name = name
  
  # Creates typing effect
  def Type(self, p1):
    for l in p1:
      print(l, end='')
      sys.stdout.flush()
      time.sleep(0.075)
    print("")

  # Prints rules
  def Rules(self):
    time.sleep(1)
    for i in rules:
      self.Type(i)
      # print("")
      time.sleep(1)

  # Prints credits
  def Credits(self):
    for l in credits:
      time.sleep(2)
      print(f"{l:^50}")

  # Choose destination
  def destination(self, p1):
    print("\nPick your location.")
    p1.display()
    place = eval(input("Enter Choice Here: "))
    return place

  # Ask question and check answer
  def check(self, p1, p2, p3):
    a = input(f"{p1} ").lower()
    if a != p2[p1].lower():
      del p3[p1]
      return False
    del p3[p1]

  # If a location runs out
  def placecheck(self, p1, p2, p3, p4, p5):
    if len(p5[p4]) == 0:
      print(f"You stayed in {p1} for too long!")
      p2.remove(p1)
      p3.pop(p4)

  def bonusq(self, p1, p2):
    bonusq = random.choice(p1)
    ans = input(f"{bonusq} ").lower()

    if ans == p2[bonusq].lower():
      Player.lives = 3
      print("Good Job! Your lives have been restored.")
      del p2[bonusq]
      return True

  def win(self, p1, p2):
    win_str = f"\nYou did it! The police have given up. You took {p1:.1f} seconds and lost {p2} lives."
    self.Type(win_str)
    self.Credits()
  
  def lose(self):
    lose_str = "\nYou have lost all of your lives. The police caught up with you. Try again!"
    self.Type(lose_str)