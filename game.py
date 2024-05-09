import random

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

  def attack(self, target):
    damage = random.randint(self.get_level() * 2, self.get_level() * 4)  
    target.being_attacked(damage)
    print(f"{self.get_name()} attacks {target.get_name()} for {damage} damage.")

  def being_attacked(self, damage):
    self.__life -= damage

    if self.__life < 0:
      self.__life = 0

class Hero(Player): 
  def __init__(self, name, life, level, skill):
    super().__init__(name, life, level)
    self.__skill = skill
  
  def get_skill(self):
      return self.__skill

  def show_details(self):
    return f"{super().show_details()}\n Skill: {self.get_skill()}\n"

  def special_attack(self, target):
    damage = random.randint(self.get_level() * 5, self.get_level() * 8) 
    target.being_attacked(damage)
    print(f"{self.get_name()} used the special skill {self.get_skill()} in {target.get_name()} for {damage} damage.")

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
    self.hero = Hero(name="Cheryl", life=100, level=5, skill="Fire Ball")
    self.enemy = Enemy(name="Mormom", life=80, level=5, type="Flyer")

  def start_batle(self): 
    print("Starting batle... ⚔️")
    
    while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
      print("Players info:")
      print(self.hero.show_details())
      print(self.enemy.show_details())

      input("Press Enter to attack... 🔥")  
      choice = input("Choose (1 - Normal Attack, 2 - Super Attack): ")

      if choice == "1":
        self.hero.attack(self.enemy)
      elif choice == "2":
        self.hero.special_attack(self.enemy)
      else:
        print("Invalid choice. Try again... ")

      if self.enemy.get_life() > 0:
        self.enemy.attack(self.hero)
      
    if self.hero.get_life() > 0:
      print(f"{self.hero.get_name()} won the battle! 🎉")
    else:
      print(f"{self.hero.get_name()} just lost! ☠️")

game = Game()
game.start_batle()