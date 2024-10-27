
from random import randint
from termcolor import colored, cprint

#TODO
# import sys
# from termcolor import colored, cprint




class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 200
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}, еды осталось {}, денег осталось {}'.format(
            self.name, self.fullness, self.food, self.money)

    def eat(self):
        if self.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.food -= 10
            self.money -= 10
        else:
            print('У {} нет еды, Пора в магазин'.format(self.name))
            self.go_shop()

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.money += 50
        self.fullness -= 10

    def go_shop(self):
        if self.money >= 50:
            print('{} сходил в магазин'.format(self.name))
            self.food += 50
            self.money -= 50
        else:
            print('У {} кончились деньги, пора Васи сходить на работу'.format(self.name))
            self.work()

    def play_dota2(self):
        print('{} поиграл в DOTA2'.format(self.name))
        self.fullness -= 10
        self.money -= 10

    def act(self):
        if self.fullness <= 0:
            print('{} умер'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.food <= 10:
            self.go_shop()
        elif self.money <= 30:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_dota2()

    def go_house(self, house):
        self.house = house
        print('{} заехал в дом'.format(self.name))
        self.fullness -= 10

class House:
    def __init__(self):
        self.food = 0
        self.money = 50




beavis = Man(name='Beavis')
batthead = Man(name='Batthead')
for day in range(1, 41):
    cprint('========================= день {} ===================='.format(day), color="yellow")
    beavis.act()
    batthead.act()
    print(beavis)
    print(batthead)

