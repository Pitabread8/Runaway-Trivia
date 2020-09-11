#logic.py has the Player() class, which has factors like player health, as well as the Logic() class, which checks the player's answer to the question

easyquestionsdict_asia = {
    "Is India in the northern hemisphere, southern hemisphere, or both?":
    "Northern",
    "What is the capital of China?":
    "Beijing",
    "What is the capital of Japan?":
    "Tokyo",
    "What is the main religion in Jordan?":
    "Islam",
    "What is the national language of India?":
    "Hindi",
    "What is the main religion in Israel?":
    "Judaism",
    "What is the capital of South Korea?":
    "Seoul"
}

easyquestionsdict_europe = {
    "What currency is used in France?":
    "Euro",
    "What is the capital of Germany?":
    "Berlin",
    "What is the capital of the United Kingdom?":
    "London"
}

mediumquestionsdict_asia = {
    "What currency is used in Indonesia?": "Rupiah",
    "What is the biggest river that flows through China?": "Yangtze River",
    "What is the national animal of China?": "Giant Panda",
    "What is the currency of Japan?": "Yen",
    "What is the national language of Myanmar?": "Burmese"
}
mediumquestionsdict_europe = {
    "What is the capital of Italy?": "Rome",
    "What is the capital of Scotland?": "Edinburgh",
    "How many countries are part of the United Kingdom?": "4"
}
mediumquestionsdict_northamerica = {
    "What is the official language of Belize?": "English",
    "What is the currency of Mexico?": "Peso"
}

hardquestionsdict_northamerica = {
    "What is the currency of the U.S?": "Dollar",
    "What is the national flower of the United States?": "Rose"
}
hardquestionsdict_europe = {
    "What currency is used by Russia?": "Ruble",
    "What is the national animal of Scotland?": "Unicorn"
}   
hardquestionsdict_asia = {
    "How many states are in India?": "29",
    "How many mountains are in Taiwan?": "260"
}
hardquestionsdict_southamerica = {  
    "What is the official language of Suriname?": "Dutch",
    "How many time zones are there in Brazil?": "4"
}
hardquestionsdict_africa = {
    "What is the capital of Morocco?": "Rabat",
    "What is the national language of Ethiopia?": "Amharic"
}

class Player():
  def __init__(self, lives = 3):
    self.lives = lives
  
  def isAlive(self):
    return self.lives > 0

  def getInfo(self):
    print(f"You have {self.lives} lives left.")  

class Logic():
  def __init__(self, answer): 
    self.answer = answer

  def EasyIsCorrect_asia(self, question):
    if self.answer == easyquestionsdict_asia[question].lower():
      return True
    else:
      return False

  def EasyIsCorrect_europe(self, question):
    if self.answer == easyquestionsdict_europe[question].lower():
      return True
    else:
      return False

  def MediumIsCorrect_asia(self, question):
    if self.answer == mediumquestionsdict_asia[question].lower():
      return True
    else:
      return False
 
  def MediumIsCorrect_europe(self, question):
    if self.answer == mediumquestionsdict_europe[question].lower():
      return True
    else:
      return False

  def MediumIsCorrect_northamerica(self, question):
    if self.answer == mediumquestionsdict_northamerica[question].lower():
      return True
    else:
      return False      

  def HardIsCorrect_asia(self, question):
    if self.answer == hardquestionsdict_asia[question].lower():
      return True
    else:
      return False
      
  def HardIsCorrect_europe(self, question):
    if self.answer == hardquestionsdict_europe[question].lower():
      return True
    else:
      return False
      
  def HardIsCorrect_africa(self, question):
    if self.answer == hardquestionsdict_africa[question].lower():
      return True
    else:
      return False

  def HardIsCorrect_northamerica(self, question):
    if self.answer == hardquestionsdict_northamerica[question].lower():
      return True
    else:
      return False
      
  def HardIsCorrect_southamerica(self, question):
    if self.answer == hardquestionsdict_southamerica[question].lower():
      return True
    else:
      return False