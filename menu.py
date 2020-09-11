#menu.py has the Menu() class, which can be used to show selection menus

import random
#class
class Menu():
  def __init__(self, lists):
    self.lists = lists
  
  def display(self):
    print("Selection Options:")
    for t in range(0, len(self.lists)):
      print(f"[{t}] {self.lists[t]}")