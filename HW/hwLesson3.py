from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self._health = health
        self.strength = strength

    def greet(self):
        return f"Привет, я {self.name}, мой уровень {self.level}"

    def rest(self):
        return f"{self.name} отдыхает"

    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        return "Воин атакует мечом"

class Mage(Hero):
    def attack(self):
        return "Маг использует магию"

class Assasin(Hero):
    def attack(self):
        return "Ассасин атакует из-под тишка"

Gimli = Warrior(name="Gimli", level=1, health=100, strength=10)
Doremor =Mage(name="Doremor", level=1, health=100, strength=10)
Wane=Assasin(name="Wane", level=1, health=100, strength=10)

print(Gimli.greet())
print(Doremor.greet())
print(Wane.greet())

print(Gimli.rest())
print(Doremor.rest())
print(Wane.rest())

print(Gimli.attack())
print(Doremor.attack())
print(Wane.attack())

