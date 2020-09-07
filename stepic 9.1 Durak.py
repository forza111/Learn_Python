c1, c2 = input().split()
trump = input()
suits = ('C', 'D', 'H', 'S')
values = {'6': 1,
          '7': 2,
          '8': 3,
          '9': 4,
          '10': 5,
          'J': 6,
          'Q': 7,
          'K': 8,
          'A': 9}


class Card:
    def __init__(self, c):
        self.suit = c[-1]
        self.value = values[c[:-1]]
        self.is_trump = self.suit == trump
        if self.is_trump:
            self.value += 10

    def __str__(self):
        return 'Value: {}, suit: {}, is trump: {}'.format(self.value, self.suit, self.is_trump)

card1 = Card(c1)
card2 = Card(c2)

if card1.suit == card2.suit or any((card1.is_trump, card2.is_trump)):
    if card1.value > card2.value:
        print('First')
    else:
        print('Second')
else:
    print('Error')
