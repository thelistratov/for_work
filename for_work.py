class Man:
    def __init__(self):
        self.strengh = 25

    def __str__(self):
        print('У {} столько сил'.format(fink_igor.strengh))


fink_igor = Man()

fink_igor.strengh += 10

print(fink_igor)
