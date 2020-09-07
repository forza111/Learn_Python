class Unit_in_game():
    def __init__(self,eyes, hair, color, pol, race):
        self.eyes = eyes
        self.hair = hair
        self.color = color
        self.pol = pol
        self.race = race
        self.year = 1
        self.klan = 'Clan Forzi'
    def inform(self):
        '''Выводит информацию о персонаже'''
        a = 'Ваш перссонаж обладает ' + self.eyes + '(ми) Глазами ' + 'Цвет волос ' + self.hair
        return a.title()

forza = Unit_in_game('Голубые','баке', 'белый', ' мужик', 'Орк')

print(forza.inform())