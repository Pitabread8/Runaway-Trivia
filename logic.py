class Player():
  def __init__(self, lives = 3):
    self.lives = lives
  
  def isAlive(self):
    return self.lives > 0

  def getInfo(self):
    print(f"You have {self.lives} lives left.")