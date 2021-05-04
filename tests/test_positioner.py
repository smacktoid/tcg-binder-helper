import unittest
from tcgbinderhelper.positioner import find_position, Side


class TestPositioner(unittest.TestCase):

    def test_first_card_is_in_first_slot_on_front_ofpage_one(self):
        position = find_position(1)
        self.assertEqual(1, position.slot)
        self.assertEqual(1, position.page)
        self.assertEqual(Side.FRONT, position.side)

    def test_eighteenth_card_is_on_ninth_slot_of_back_of_page_one(self):
        position = find_position(18)
        self.assertEqual(9, position.slot)
        self.assertEqual(1, position.page)
        self.assertEqual(Side.BACK, position.side)

    def test_page_calculated_correctly_after_first_page(self):
        position = find_position(19)
        self.assertEqual(2, position.page)
        self.assertEqual(1, position.slot)
        self.assertEqual(Side.FRONT, position.side)


if __name__ == '__main__':
    unittest.main()