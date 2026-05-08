#---инкапсуляция---- public, _protect, __private
class BankAccount:
    def __init__(self, login, balance, password):
        self.login = login
        self._balance = balance #зашещенные должны работать только внутри класса или подкласса
        self.__password = password #приватная

class VipsAccount(BankAccount):
    def get_balance(self):
        print(self._balance)
    # def get_password(self):
    #     print(self.__password)
    def _hidden(self):
        pass
    def __secret(self):
        pass

    def user(self):
        self._hidden()
        self.__secret()



consumer = BankAccount(login="admin", balance=1000, password="12345")
vip_member = VipsAccount(login="vips", balance=2000, password="zzzz")

print(consumer.login)
print(consumer._balance)
print(consumer._BankAccount__password)
print(vip_member.login)
print(vip_member._balance)
# print(vip_member__password)
print(dir(consumer))



#-----abstraction-----
from abc import ABC, abstractmethod
#абстрактный класс - обязательные методы которые должны быть реализованы в подклассе
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def action(self):
        pass

#Дочерний класс
class Dog(Animal):
    def action(self):
        print("Run")

    def make_sound(self):
        print("RRRRR")

class Duck(Animal):
    def make_sound(self):
        print("Gak Gak")

    def action(self):
        print("Fly")

duckkie = Duck()
duckkie.make_sound()
# duckkie.action()




guffi = Dog()

guffi.make_sound()
guffi.action()