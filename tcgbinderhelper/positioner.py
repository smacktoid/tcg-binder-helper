class CardPosition(object):
    def __init__(self, page, slot):
        self.page = page
        self.slot = slot




def find(card_number)->CardPosition:
    print(f'Finding position for card {card_number}')
    slot = card_number % 18
    return CardPosition(0, slot)
