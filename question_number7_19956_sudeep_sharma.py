from scipy.stats import t
import numpy as np
import matplotlib.pyplot as plt
import datetime
print(datetime.datetime.now())
# Step 1: Generate 100 random numbers from t-distribution with df=10
df = 10  # degrees of freedom
random_numbers = t.rvs(df, size=100)

# Step 2: Calculate mean μ and standard deviation σ of these numbers
mu = np.mean(random_numbers)
sigma = np.std(random_numbers)

# Step 3: Create 15 sampling groups, each with 30 samples
num_samples = 30
num_groups = 15
sampling_group_means = []

for _ in range(num_groups):
    sample = np.random.choice(random_numbers, size=num_samples, replace=False)
    sampling_group_means.append(np.mean(sample))

# Step 4: Calculate the mean of the sampling group means
mean_of_means = np.mean(sampling_group_means)

# Step 5: Verify CLT
# The standard deviation of the sample means (σx) should be close to σ/√n
sigma_x = np.std(sampling_group_means)
expected_sigma_x = sigma / np.sqrt(num_samples)

print(f'mean : {round(mu,4)}')
print(f' standard deviation  is {round(sigma,4)}')
print(f'mean of the sampling group means is {round(mean_of_means,4)}')
print(f'standard deviation of the sampling group means is {round(sigma_x,4)}')
print(f'Expected standard deviation of the sample means is {round(expected_sigma_x,4)}')
# Step 6: Plot histogram of the sample means
plt.hist(sampling_group_means, bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel('Sample Means')
plt.ylabel('Frequency')
plt.title('Histogram of Sample Means')
plt.show()

(mu, sigma, mean_of_means, sigma_x, expected_sigma_x)

