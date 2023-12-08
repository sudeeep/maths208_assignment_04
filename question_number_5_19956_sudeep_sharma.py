# Parameters
import numpy as np
from scipy.stats import  norm
import datetime
print(datetime.datetime.now())


n = 12  # Number of coin tosses
p = 0.5  # Probability of getting heads

# Mean and standard deviation for the normal approximation
mu = n * p
sigma = np.sqrt(n * p * (1 - p))

# Apply continuity correction and calculate probability using normal distribution
# Probability of getting exactly 6 heads
normal_prob_exact_6 = norm.cdf(6.5, mu, sigma) 
print("normal probality of exact 6 head",normal_prob_exact_6)
