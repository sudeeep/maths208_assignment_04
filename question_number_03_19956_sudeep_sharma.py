import numpy as np
import datetime
print(datetime.datetime.now())
# Given probability and sample size
p = 0.05
n = 51  # choosing n greater than 50

# Calculating the expected mean and standard deviation
expected_mean = n * p
q = 1 - p  # q is the probability of failure
expected_std_dev = (n * p * q) ** 0.5

# Simulating a binomial distribution
np.random.seed(0)  # Seed for reproducibility
simulated_data = np.random.binomial(n, p, 10000)  # Simulating 10,000 trials

# Calculating the sample mean and standard deviation
sample_mean = np.mean(simulated_data)
sample_std_dev = np.std(simulated_data)

print(f'expected mean is {round(expected_mean,4)} and sample mean is {round(sample_mean,4)}')
print(f'standard deviation  is {round(expected_std_dev,4)} and sample standard deviation  is {round(sample_std_dev,4)}')


