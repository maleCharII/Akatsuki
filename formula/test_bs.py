import unittest
from .. import bs

class TestBS(unittest.TestCase):

    def get_input(self) -> dict:
        input = {
            'opt_code': 1,
            'F': 373, 
            'K': 365, 
            'sigma': 0.25, 
            't': 1/360,
        }
        return input

    def price_is_positive(self):
        print("testing: option price should be positive...")
        input = self.get_input()

        for i in (bs.CALL, bs.PUT):
            style = 'Call' if i == 1 else 'Put'
            input['opt_code'] = i
            
            p = bs.price(1, 372, 372, 0.2, 1/252)
            self.assertGreater(p, 0, f"{style} option price is positive")

unittest.main()
