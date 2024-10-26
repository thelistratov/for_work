class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 200

    def __str__(self):
        return 'Я - {}, сытость {}, еды осталось {}, денег осталось {}'.format(
            self.name, self.fullness, self.food, self.money)

    def eat(self):
        if self.food > 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.food -= 10
            self.money -= 10
        else:
            print('{} нет еды'.format(self.name))
    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.money += 50
        self.fullness -= 10

    def play_DOTS(self):
        print('{} поиграл в DOTA2'.format(self.name))
        self.fullness -= 10


vasya = Man(name='Вася')
for day in range(1,21):
    print('========================= день {} ===================='.format(day))
    vasya.act()
    print()
