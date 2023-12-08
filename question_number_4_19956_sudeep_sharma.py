from scipy.stats import binom, norm
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Print current datetime
current_datetime = datetime.datetime.now()
print("Current datetime:", current_datetime)

# Define the parameters
n = 50  # number of trials
p = 0.5  # probability of success
q = 1 - p  # probability of failure
k = 25  # number of successes

# Calculate the exact binomial probability
binomial_prob = binom.pmf(k, n, p)

# Approximate using the normal distribution
mu = n * p  # mean
sigma = np.sqrt(n * p * q)  # standard deviation

# Convert the binomial problem to a normal distribution problem
normal_prob = norm.cdf(k + 0.5, mu, sigma) - norm.cdf(k - 0.5, mu, sigma)

# Print probabilities
print(f"Binomial probability: {binomial_prob}, Normal probability: {normal_prob}")

# Generate binomial distribution data
x = np.arange(0, n+1)
binom_dist = binom.pmf(x, n, p)

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(x, binom_dist, color='blue', alpha=0.7, label='Binomial Distribution')
plt.axvline(x=k - 0.5, color='red', linestyle='dashed', linewidth=2)
plt.axvline(x=k + 0.5, color='red', linestyle='dashed', linewidth=2)
plt.fill_between(x, binom_dist, where=(x >= k - 0.5) & (x <= k + 0.5), color='red', alpha=0.5,
                 label='Normal Approximation Area')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.title('Binomial Distribution vs. Normal Approximation')
plt.legend()
plt.grid(True)
plt.show()
