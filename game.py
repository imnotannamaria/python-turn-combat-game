class Player:
  def __init__(self, name, life, level):
    self.__name = name
    self.__life = life
    self.__level = level

  def get_name(self):
    return self.__name

  def get_life(self):
    return self.__life

  def get_level(self):
    return self.__level

  def show_details(self):
    return f"Name: {self.get_name()}\nLife: {self.get_life()}\nLevel: {self.get_level()}"

class Hero(Player): 
  def __init__(self, name, life, level, skill):
    super().__init__(name, life, level)
    self.__skill = skill
  
  def get_skill(self):
      return self.__skill

  def show_details(self):
    return f"{super().show_details()}\n Skill: {self.get_skill()}\n"

class Enemy(Player): 
  def __init__(self, name, life, level, type):
    super().__init__(name, life, level)
    self.__type = type
  
  def get_type(self):
    return self.__type

  def show_details(self):
    return f"{super().show_details()}\n Type: {self.get_type()}\n"

class Game: 
  def __init__(self) -> None:
    self.hero = Hero(name="Biro", life=100, level=1, skill="Cry")
    self.enemy = Enemy(name="Leo", life=100, level=1, type="Flyer")

  def start_batle(self): 
    print("Starting batle... ⚔️")
    
    while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
      print("Players info:")
      print(self.hero.show_details())
      print(self.enemy.show_details())

      input("Press Enter to attack... 🔥")  
      choice = input("Choose (1 - Normal Attack, 2 - Super Attack): ")

game = Game()
game.start_batle()