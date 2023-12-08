# Define the means and standard deviations of X and Y
import datetime
print(datetime.datetime.now())
mu_X = 10  # Mean of X
sigma_X = 3  # Standard deviation of X
mu_Y = 15  # Mean of Y
sigma_Y = 8  # Standard deviation of Y

# Calculate the mean and standard deviation for X + Y
mu_X_plus_Y = mu_X + mu_Y
sigma_X_plus_Y = (sigma_X**2 + sigma_Y**2)**0.5

# Calculate the mean and standard deviation for X - Y
mu_X_minus_Y = mu_X - mu_Y
sigma_X_minus_Y = (sigma_X**2 + sigma_Y**2)**0.5

# Calculate the mean and standard deviation for 3X
mu_3X = 3 * mu_X
sigma_3X = 3 * sigma_X

# Calculate the mean and standard deviation for 4X + 5Y
mu_4X_plus_5Y = 4 * mu_X + 5 * mu_Y
sigma_4X_plus_5Y = ((4 * sigma_X)**2 + (5 * sigma_Y)**2)**0.5

# Print the results
print(f"Mean and Standard Deviation for X + Y:  , mean :{mu_X_plus_Y}  , standard deviation:{sigma_X_plus_Y}")
print(f"Mean and Standard Deviation for X - Y:  , mean:{mu_X_minus_Y}   , standard deviation {sigma_X_minus_Y}")
print(f"Mean and Standard Deviation for 3X:     mean:{ mu_3X }   , standard_deviation {sigma_3X}")
print(f"Mean and Standard Deviation for 4X + 5Y:, mean: {mu_4X_plus_5Y}  , standard deviation:{sigma_4X_plus_5Y}")
