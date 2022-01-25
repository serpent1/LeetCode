# import sys
# import timeit
#
# a = list(range(10000,100000,10000))
# b = tuple(range(100000))
# print(sys.getsizeof(a), sys.getsizeof(b))    # 900120 800056
#
# print(timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]'))
# print(timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)'))
# print(a)

#
#
from enum import Enum


class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)

class Card:
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # 根据牌的花色和点数取到对应的字符
        return f'{suites[self.suite.value]}{faces[self.face]}'

    def __lt__(self, other):
        # 花色相同比较点数的大小
        if self.suite == other.suite:
            return self.face < other.face
        # 花色不同比较花色对应的值
        return self.suite.value < other.suite.value


# card2 = Card(Suite.HEART, 13)
# print(card1, card2)    # ♠5 ♥K
#
#
# for suite in Suite:
#     print(f'{suite}: {suite.value}')


import random


class Poker:
    """扑克"""

    def __init__(self):
        # 通过列表的生成式语法创建一个装52张牌的列表
        self.cards = [Card(suite, face) for suite in Suite
                      for face in range(1, 14)]
        # current属性表示发牌的位置
        self.current = 0

    def shuffle(self):
        """洗牌"""
        self.current = 0
        # 通过random模块的shuffle函数实现列表的随机乱序
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self.current < len(self.cards)

# poker = Poker()
# poker.shuffle()
# print(poker.cards)
class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()

poker = Poker()
poker.shuffle()
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())
        #print('{0}{1}'.format(player.name,player.cards))

for player in players:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(player.cards)