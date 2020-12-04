import random

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
      return False
    del p3[p1]

  # If a location runs out
  def placecheck(self, p1, p2, p3, p4):
    print(f"You stayed in {p1} for too long!")
    p2.remove(p1)
    p3.pop(p4)