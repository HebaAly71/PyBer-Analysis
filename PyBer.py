# %%
# Add Matplotlib inline magic command
%matplotlib inline
# %%
# Libraries needed
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics 
#%%
#Load the city and ride data
city_data_to_load = "/Users/hebamaly/PyBer-Analysis/Resources/city_data.csv"
ride_data_to_load = "/Users/hebamaly/PyBer-Analysis/Resources/ride_data.csv"
#%%
# Read the city data file and store it in a pandas DataFrame.
city_data_df = pd.read_csv(city_data_to_load)
city_data_df.head(10)
#%%
# Read the ride data file and store it in a pandas DataFrame.
ride_data_df = pd.read_csv(ride_data_to_load)
ride_data_df.head(10)
# %%
# Get the columns and the rows that are not null.
city_data_df.count()
# %%
# Get the data types of each column.
city_data_df.dtypes
# %%
# Get the unique values of the type of city.
#city_data_df["type"].unique()
city_data_df["type"].unique()
# %%
# Get the number of data points from the Urban cities.
sum(city_data_df["type"]=="Urban")
# %%
# Get the number of data points from the Suburban cities.
sum(city_data_df["type"]=="Suburban")
# %%
# Get the number of data points from the Rural cities.
sum(city_data_df["type"]=="Rural")
# %%
# Get the columns and the rows that are not null.
ride_data_df.count()
# %%
# Get the data types of each column.
ride_data_df.dtypes

# %%
# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, how="left", on=["city", "city"])

# Display the DataFrame
pyber_data_df.head()

# %%
