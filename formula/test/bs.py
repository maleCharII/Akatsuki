import unittest
# import formula.bs as bs

import ...draft

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

    def test_price_is_positive(self):
        input = self.get_input()

        for i in (bs.CALL, bs.PUT):
            style = 'Call' if i == 1 else 'Put'
            input['opt_code'] = i
            
            p = bs.price(**input)
            self.assertGreater(p, 0, f"\n{style} option price should be positive")



print("-"*70)
unittest.main()

