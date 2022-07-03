# pytest automatically do this ... so only for debug purpose 
# if __package__ is None:
#     
import formula.bs as bs


def test_price_is_positive():
    input = {
            'opt_code': 1,
            'F': 373, 
            'K': 365, 
            'sigma': 0.25, 
            't': 1/360,
        }

    price = bs.price(**input)
    assert price > 0






