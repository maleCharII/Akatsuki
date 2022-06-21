from formula import bs
import numpy as np
from scipy.stats import norm

F = 369
K = 369
sigma = .2
t = 1/252

p = bs.price(0, F, K , sigma, t)
print(p)

# compute numerical delta
d = bs.price(0, F + 1, K , sigma, t) - p
print(d)



print(np.isnan(np.NAN))
