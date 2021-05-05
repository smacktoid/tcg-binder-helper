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

    def test_position_description_front_slot(self):
        position = find_position(5)
        self.assertEqual('Front of page 1, slot 5', position.description())

    def test_position_description_back_slot(self):
        position = find_position(30)
        self.assertEqual('Back of page 2, slot 3', position.description())

    def test_position_includes_card_sequence_for_page(self):
        position = find_position(19)
        expected_sequence = range(19, 28)

        self.assertEqual(expected_sequence, position.page_card_sequence)

if __name__ == '__main__':
    unittest.main()