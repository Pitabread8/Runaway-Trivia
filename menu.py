class Menu():
  def __init__(self, lists):
    self.lists = lists
  
  def display(self):
    print("Selection Options:")
    for t in range(0, len(self.lists)):
      print(f"[{t}] {self.lists[t]}")