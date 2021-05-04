import unittest
from tcgbinderhelper import positioner


class TestPositioner(unittest.TestCase):

    def test_first_card_is_in_first_slot_on_page_one(self):
        position = positioner.find(1)
        self.assertEqual(1, position.slot)

if __name__ == '__main__':
    unittest.main()