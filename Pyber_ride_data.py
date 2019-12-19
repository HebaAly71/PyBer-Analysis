#%%
%matplotlib inline
#%%
# Libraries needed
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics 
#%%
#Load and read file
pyber_ride_df = pd.read_csv("/Users/hebamaly/PyBer-Analysis/Resources/PyBer_ride_data.csv")
pyber_ride_df

# %%
# Set x-axis and tick locations.
x_axis = np.arange(len(pyber_ride_df), step=5.0)
tick_locations = [value for value in x_axis]
# Plot the data.
pyber_ride_df.plot(x="Month", y="Avg. Fare ($USD)")
plt.xticks(tick_locations, pyber_ride_df["Month"])
plt.show()

# %%
#Plot a bar chart to the data
pyber_ride_df.plot.bar(x="Month", y="Avg. Fare ($USD)")
plt.show()

# %%
#Calculate the error by getting standard deviation for Avg fares
stdev_avg_fare = statistics.stdev(pyber_ride_df['Avg. Fare ($USD)'])
stdev_avg_fare

# %%
#Plot the data 
pyber_ride_df.plot.bar(x='Month', y='Avg. Fare ($USD)', yerr=stdev_avg_fare, capsize=3, color='skyblue')
# Setup the major ticks by $5
plt.yticks(np.arange(0, 51, step=5.0))
#Rotate x labels to horizontal
plt.xticks(rotation=0)
#plt.yticks(tick_locations, pyber_ride_df["Avg. Fare ($USD)"])
plt.show()

# %%

# %%
