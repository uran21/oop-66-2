import random

class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень: {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")

    def rest(self):
        self.health += 10
        print(f"{self.name} отдыхает. Здоровье восстановлено до {self.health}")

class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name} (Воин) атакует мечом! (Выносливость: {self.stamina})")

class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name} (Маг) кастует заклинание! (Мана: {self.mana})")

class Assasin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name} (Ассасин) атакует из-под тишка! (Скрытность: {self.stealth})")

warrior_obj = Warrior("Gimili", 10, 100, 20, 50)
mage_obj = Mage("Gandalf", 12, 80, 15, 100)
assasin_obj = Assasin("Ezio", 11, 90, 18, 40)

hero_types = ["Warrior", "Mage", "Assasin"]

user_choice = input("Выберите героя: Warrior / Mage / Assasin: ").strip().capitalize()
enemy_type = random.choice(hero_types)

print(f"Вы выбрали: {user_choice}")
print(f"Противник: {enemy_type}")

if user_choice == enemy_type:
    print("Ничья!")
elif (user_choice == "Warrior" and enemy_type == "Assasin") or \
        (user_choice == "Assasin" and enemy_type == "Mage") or \
        (user_choice == "Mage" and enemy_type == "Warrior"):

    if user_choice == "Warrior":
        warrior_obj.attack()
    elif user_choice == "Mage":
        mage_obj.attack()
    else:
        assasin_obj.attack()

    print(f"{user_choice} победил!")
else:
    if enemy_type == "Warrior":
        warrior_obj.attack()
    elif enemy_type == "Mage":
        mage_obj.attack()
    else:
        assasin_obj.attack()

    print(f"{enemy_type} победил!")