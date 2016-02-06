from math import sqrt

class kwadratowa(object):
    def __init__(self):
        self.delta1 = 0
        self.delta2 = 0
        self.a = 0
        self.b = 0
        self.c = 0
        self.x1 = 0
        self.x2 = 0

    def delta(self):
        self.delta1 = self.b ** 2 - (4 * self.a * self.c)
        if self.delta1 >= 0:
            self.delta2 = sqrt(self.delta1)
        else:
            print 'Rownanie o podanych parametrach nie ma rozwiazan'

    def wynik(self):
        self.x1 = (-1 * self.b - self.delta2) / 2 * self.a
        self.x2 = (-1 * self.b + self.delta2) / 2 * self.a

    def podajwartosci(self):
        self.a = raw_input('Podaj a:')
        self.b = raw_input('Podaj b:')
        self.c = raw_input('Podaj c:')
        self.a = float(self.a)
        self.b = float(self.b)
        self.c = float(self.c)
        self.obliczenia()

    def obliczenia(self):
        if self.a > 0 or self.a < 0:
            self.delta()
            self.wynik()
            if self.delta1 > 0:
                print 'Wynik to x1=%s oraz x2=%s' % (self.x1, self.x2)
            elif self.delta1 == 0:
                print 'Wynik to x=%s' % self.x1
        else:
            print 'Wspolczynnik A nie moze byc rowny 0'

        return self.podajwartosci()





