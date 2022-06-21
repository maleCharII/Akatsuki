import numpy as np
from scipy.stats import norm

# option code
CALL = 1
PUT = 0

def price(opt_code, F, K, sigma, t) -> np.double:
    """
    Black-Scholes pricing formula
    Forward convention, non-discounting
    """

    if opt_code != 1 and opt_code != 0:
        # not explicit raise for broadcasting usage    
        return np.nan        

    vol = sigma * np.sqrt(t)
    d1 = np.log(F/K) + .5 * vol * vol
    d2 = d1 - vol
    sign = opt_code * 2 - 1

    return sign * norm.cdf(sign*d1) * F - sign * norm.cdf(sign*d2) * K
    
def delta():
    pass

