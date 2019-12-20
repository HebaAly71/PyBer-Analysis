# %%
# Add Matplotlib inline magic command
%matplotlib inline
# %%
# Libraries needed
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics 
import scipy.stats as sts
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
# Part 1 
#Calculate the total fares and driver count by city type
pyber_groupbycitytype=pyber_data_df.groupby('type')
pyber_groupbycitytype_total=pyber_groupbycitytype['fare','driver_count'].sum() 
pyber_groupbycitytype_total

# %%
#Calculate the total rides by city type
pyber_groupbycitytype_count=pyber_groupbycitytype['ride_id'].count()
# %%
# Add the total rides series into the pybergroupcitytype_total dataframe
pyber_groupbycitytype_total['Total Rides'] =  pyber_groupbycitytype_count
pyber_groupbycitytype_total
# %%
# Calculate the average fare per ride
Avg_fare_per_ride = pyber_groupbycitytype_total['fare'] / pyber_groupbycitytype_total['Total Rides']
Avg_fare_per_ride

# %%
# Calculate the average driver per ride
Avg_driver_per_ride = pyber_groupbycitytype_total['driver_count'] / pyber_groupbycitytype_total['Total Rides']
Avg_driver_per_ride

# %%
# Calculate the average fare per driver
Avg_fare_per_driver = pyber_groupbycitytype_total['fare'] / pyber_groupbycitytype_total['driver_count']
Avg_fare_per_driver

# %%
# Add Average fare per driver and ride as columns in the summary table
pyber_groupbycitytype_total['Average Fare per Ride'] =  Avg_fare_per_ride
pyber_groupbycitytype_total['Average Fare per Driver'] =  Avg_fare_per_driver
pyber_groupbycitytype_total

# %%
# Formatting average fare per driver
pyber_groupbycitytype_total['Average Fare per Ride'] = pyber_groupbycitytype_total['Average Fare per Ride'].map("${:,.2f}".format)
# %%
# Formatting average fare per driver
pyber_groupbycitytype_total['Average Fare per Driver'] = pyber_groupbycitytype_total['Average Fare per Driver'].map("${:,.2f}".format)
# %%
# Fromatting total fare
pyber_groupbycitytype_total['fare'] = pyber_groupbycitytype_total['fare'].map("${:,.2f}".format)


# %%
#Rename the summary table column name
pyber_groupbycitytype_total = pyber_groupbycitytype_total.rename(columns={"driver_count":"Total Drivers", "fare":"Total Fares"})

# %%
# Delete Index name
del pyber_groupbycitytype_total.index.name
# %%
# Summary Table by City Type
pyber_groupbycitytype_total

# %%
# Part 2
# Rename column in the merged Dataframe
pyber_data_df = pyber_data_df.rename(columns={'city': 'City', 'date':'Date','fare':'Fare', 'ride_id': 'Ride Id','driver_count': 'No. Drivers', 'type':'City Type'})

# %%
# Set index to Date
pyber_data_df.set_index('Date')
# %%
# Copy The dataframe and create a fare dataframe
pyber_data_fare_df = pyber_data_df[['Date', 'City Type', 'Fare']].copy()
pyber_data_fare_df

# %%
# Set index to Date
pyber_data_fare_df_new = pyber_data_fare_df.set_index('Date')

# %%
type(pyber_data_fare_df_new.index)
# %%
# Set index datetime data type
pyber_data_fare_df_new.index.astype('datetime64[ns]')

# %%
# Make sure the index data type is date time
pyber_data_fare_df_new.info()

# %%
pyber_data_fare_df_new

# %%
