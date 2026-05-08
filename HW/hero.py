class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength 

    def greet(self): 
        print(f"Hello, I am {self.name}, my level is {self.level}")

    def attack(self): 
        self.strength -= 1
        print(f"{self.name} is attacking! Strength reduced to {self.strength}")

    def rest(self):
        self.strength += 1
        print(f"{self.name} is resting... Strength increased to {self.strength}")


motaro = Hero("Motaro", 101, 100, 50)
shao_kahn = Hero("Shao Kahn", 150, 200, 80)


print(f"{motaro.name}")
motaro.greet()
motaro.attack() 
motaro.rest()   
print(f"\n")
print(f"{shao_kahn.name}")
shao_kahn.greet()
shao_kahn.attack()
shao_kahn.attack() 
shao_kahn.rest()
