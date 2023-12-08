# Redefine parameters for this case
import numpy as np
from scipy.stats import  norm
import datetime
print(datetime.datetime.now())
n = 150  # number of batteries
p = 0.06  # defect rate

# Mean and standard deviation for the normal approximation
mu = n * p
sigma = np.sqrt(n * p * (1 - p))

# Apply continuity correction for 11.5 (to find probability of 12 or more)
normal_prob_12_or_more =1- norm.cdf(11.5, mu, sigma)

print("probality of 12 or more defective :",normal_prob_12_or_more)

