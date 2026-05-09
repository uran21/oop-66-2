class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою!"

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__( name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"


class WarriorHero(MageHero):
    def action(self):
        return f"Воин {self.name} рубит мечем! Уровень: {self.lvl}"


class BankAccount(WarriorHero):
    bank_name="Simba"

    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self._bank_name = bank_name

    def login(self):
        return self.__password

    def full_info(self):
        return self._balance

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    @staticmethod
    def bonus_for_level():
        return f"lvl * 10"

    def __str__(self):
        return f"{self.name}|Баланс:{self._balance} SOM"

    def __add__(self, other):
       if type(self.hero) == type(other.hero):
           return self.hero + other.hero
       else:
           return "Нельзя складывать разные типы героев"

    def __eq__(self, other):
        if type(self.lvl) and type(self.hero) == type(other.lvl) and type(other.hero):
            return "Одинаковые герои"
        else:
            return "Разные герои"

mage1 = MageHero("Merlin", 80, 500, 150)
mage2 = MageHero("Merlin", 80, 500, 200)
warrior = WarriorHero("Conan", 50, 900, 20)
acc1 = BankAccount(mage1, 5000, "1234", "Simba")
acc2 = BankAccount(mage2, 3000, "0000", "Simba")
acc3 = BankAccount(warrior, 2500, "1111", "Simba")

print(mage1.action())
print(mage1.action())
print(warrior.action())
print(acc1)
print(acc2)
