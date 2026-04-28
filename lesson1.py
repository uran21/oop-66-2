class Hero:
    #Констуктор класса
    def __init__(self, name, lvl, hp):
        #Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
    #Методы класса
    def action(self):
        return f"{self.name} base action!"




kirito = Hero("kirito", 1, 5)
alimar= Hero("alimar", 1, 5)

print(kirito.action())
print(alimar.action())
#class myInt:

#    pass


#my_int = MyInt(123)



#объект\экземплар но осное класса
#kirito = Hero("Kirito", 100, 10000)
#asuna = Hero("Asuna", 101, 10001)
#print(kirito.name)
#print(asuna.name)