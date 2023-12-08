import scipy.stats as stats
import datetime
print(datetime.datetime.now())
# Given data
mean = 10.3  # mean length of anchovies in cm
std_dev = 0.65  # standard deviation in cm

# Part a: Probability of anchovies being less than 9 cm
length_a = 9
prob_less_than_9cm = (stats.norm.cdf(length_a, mean, std_dev))*100

# Part b: Probability of anchovies being between 9.5 cm and 10.6 cm
length_b1 = 9.5
length_b2 = 10.6
prob_between_9_5_and_10_6cm = (stats.norm.cdf(length_b2, mean, std_dev) - stats.norm.cdf(length_b1, mean, std_dev))*100

# Part c: Minimum length if in the top 20%
# To find this, we need the 80th percentile (since top 20% means above 80% of the distribution)
percentile_c = 80
min_length_top_20_percent = stats.norm.ppf(percentile_c / 100, mean, std_dev)

# Displaying the results
print( f"probality of  Americina Anochovies less than 9 cm in percentage is { prob_less_than_9cm:2f}%") 
print( f"probality of Americian Anochives between  9.5 cm and 10.6 cm  in percentage is { (prob_between_9_5_and_10_6cm)}%") 
print( f"probality of Americian  Anochives minimum lenght for top 20 %  {min_length_top_20_percent} ") 


