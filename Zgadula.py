import random

class Zgadula(object):
    def __init__(self):
        self.wylosowaneSlowo = []
        self.ilosc_liter = None
        self.words = ['kartofel', 'ziemniak', 'pies', 'papieros']
        self.wprowadzoneZnaki = []

    def zacznijGre(self):
        self.ilosc_liter = 1
        self.losujSlowo()
        print "Jakie to slowo?"


    def losujSlowo(self):
        self.wprowadzoneZnaki = []

        self.wylosowaneSlowo = list(self.words[random.randrange(0, len(self.words))])
        for i in self.wylosowaneSlowo:
            self.wprowadzoneZnaki.append("_")
        self.wprowadzZnak(self.wylosowaneSlowo[0])

    def wprowadzZnak(self, znak):
        if znak in self.wylosowaneSlowo:
                self.wprowadzoneZnaki[self.wylosowaneSlowo.index(znak)] = znak
                self.wylosowaneSlowo[self.wylosowaneSlowo.index(znak)] = ""

        print "".join(self.wprowadzoneZnaki)
        for znak in self.wprowadzoneZnaki:
            if znak=="_":
                self.wprowadzZnak(raw_input("Zgadnij znak:"))

        print "Gratulacje ! Zgadles ! Slowo to %s" % "".join(self.wprowadzoneZnaki)
        return self.losujSlowo()
