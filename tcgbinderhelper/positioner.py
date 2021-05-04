import math
from enum import Enum


class Side(Enum):
    FRONT = 1
    BACK = 2


class CardPosition(object):
    def __init__(self, page, slot, side: Side):
        self.page = page
        self.slot = slot
        self.side = side


def find_position(card_number) -> CardPosition:
    print(f'Finding position for card {card_number}')
    slot = card_number % 18
    if slot == 0:
        slot = 18

    if slot > 9:
        slot = slot - 9
        side = Side.BACK
    else:
        side = Side.FRONT

    page = math.ceil(card_number / 18)
    return CardPosition(page, slot, side)
