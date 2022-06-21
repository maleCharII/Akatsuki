import unittest
from .. import bs

class TestBS(unittest.TestCase):

    def price_is_positive(self):
        p = bs.price(1, 372, 372, 0.2, 1/252)
        self.assertGreater(p, 0, "Price is positive")



unittest.main()
