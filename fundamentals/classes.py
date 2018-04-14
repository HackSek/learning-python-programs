class Fighter:

    sport = 'MMA'

    def __init__(self, name, weight_class, organization, champion):
        self.name = name
        self.weight_class = weight_class
        self.organization = organization
        self.champion = champion

    @classmethod
    def pre_annouce_memorable_line(cls):
        return f'And for this week\'s memorable {cls.sport} line:'


    def annouce_memorable_line(self):
        if self.champion == True:
            return f'"And STILL! the undisputed {self.organization} {self.weight_class} champion of the world ... {self.name.upper()} !!!"'

    @staticmethod
    def conclude(outro = 'thank you for tuning in to this week\'s MMA line, see ya next week!'):
        return outro

DJ = Fighter('Demetrious Johnson', 'Flyweight', 'UFC', True)

print(Fighter.pre_annouce_memorable_line())
print(DJ.annouce_memorable_line())
print(Fighter.conclude())
