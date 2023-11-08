## Name: Jaewon Son
## Date: November 07 2023
## Honor Statement: I have not given or received any unauthorized assistance on this assignment.
## Link: https://youtu.be/Wvhm6Tb7L1s


import pandas as pd
import matplotlib.pyplot as plt


# Read the CSV file
height_weight_df = pd.read_csv("C:\\Users\\LG\\Desktop\\DEPAUL UNIV\\2023 Fall\\Python Programming\\DSC 430 - Week 9\\HeightsAndWeights.csv")

# Separate data into male and female groups
height_weight_df_male = height_weight_df[height_weight_df['Sex'] == 'Male']
height_weight_df_female = height_weight_df[height_weight_df['Sex'] == 'Female']

# Create a figure and axis
fig, ax = plt.subplots()

# Scatter plot for male and female heights and weights
ax.scatter(height_weight_df_male['Height'], height_weight_df_male['Weight'], label = 'Male', color = 'blue', alpha = 0.5)
ax.scatter(height_weight_df_female['Height'], height_weight_df_female['Weight'], label = 'Female', color = 'red', alpha = 0.5)

# Define the linear regression equation parameters
slope = 0.28
intercept = 23.2

# Calculate the regression line endpoints
x1 = height_weight_df['Height'].min()
x2 = height_weight_df['Height'].max()
y1 = slope * x1 + intercept
y2 = slope * x2 + intercept

# Plot the regression line
plt.plot([x1, x2], [y1, y2], label = f'Linear Regression Line: y = {slope}x + {intercept}', color='green')

# Calculate the means and standard deviations for height and weight
height_mean = height_weight_df['Height'].mean()
height_std = height_weight_df['Height'].std()
weight_mean = height_weight_df['Weight'].mean()
weight_std = height_weight_df['Weight'].std()

# Highlight outlier regions with vertical and horizontal lines
height_lower_bound = height_mean - 2.5 * height_std
height_upper_bound = height_mean + 2.5 * height_std
weight_lower_bound = weight_mean - 2.5 * weight_std
weight_upper_bound = weight_mean + 2.5 * weight_std

# Plot vertical and horizontal lines
plt.axvline(x = height_lower_bound, color = 'orange', linestyle = '--', label = 'Height Lower Bound')
plt.axvline(x = height_upper_bound, color = 'orange', linestyle = '--', label = 'Height Upper Bound')
plt.axhline(y = weight_lower_bound, color = 'orange', linestyle = '--', label = 'Weight Lower Bound')
plt.axhline(y = weight_upper_bound, color = 'orange', linestyle = '--', label = 'Weight Upper Bound')

# Define the bounds for outliers
def is_outlier(x, mean, std):

    return (x < mean - 2.5 * std) or (x > mean + 2.5 * std)

# Find and label outliers
outliers = height_weight_df.apply(lambda row: is_outlier(row['Height'], height_mean, height_std) and is_outlier(row['Weight'], weight_mean, weight_std), axis = 1)

for i, outlier in enumerate(outliers):    
    if outlier:
        ax.text(height_weight_df['Height'].iloc[i], height_weight_df['Weight'].iloc[i], 'Outlier', fontsize = 8, color = 'purple')

# Label axes, title, and create lengend
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Height - Weight Correlation')
plt.legend()

# Show the plot
plt.show()