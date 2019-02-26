


class Soldier:
    health = 100
    def __init__(self,name):
        self.name = name

    def hit(self):
        print("Ваш герой ударил противника")

    def get_git(self):
        self.health = self.health - 20


unit1 = Soldier("Nikita")
unit2 = Soldier("Vlad")

while unit1.health > 0 and unit2.health > 0:
    n = int(input("введите номер героя"))
    if n == 1:
        Soldier.get_git(unit1)
    else:
        Soldier.get_git(unit2)

if unit1.health > unit2.health:
    print(unit1.name, "1победил")
else:
    print(unit2.name ," победил")
