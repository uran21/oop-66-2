class Fighter:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

    def action(self):
        return f"My name is {self.name}, my health is {self.hp} and my level {self.level} points."

class Hunter(Fighter):
    def __init__(self, name, hp, level, timer):
        super().__init__(name, hp, level)
        self.timer = timer

    def reload(self):
        return f"Reloading... in {self.timer}"

karate = Fighter("Bruce", "100", 1)
eagle = Hunter("Eagle", "50", 1, 20)

# print(karate.action())
# print(eagle.action())
#Method resolution ordering - что встритит первым то и выдаст
class Fly:
    def action_fly(self):
        return f"Flying..."
class Swim:
    def action_swim(self):
        return f"Swim..."
class Animal(Fly, Swim):
    def action(self):
        return f"Walking..."

# duck = Animal()
# print(duck.action_fly())
# print(duck.action_swim())
# print(duck.action())

class A:
    def action(self):
        print("A")
class B(A):
    def action(self):
        super().action()
        print("B")
class C(B):
    def action(self):
        super().action()
        print("C")
class D(C,B):
    def action(self):
        super().action()
        print("D")

test = D()
test.action()
print(D.__mro__)