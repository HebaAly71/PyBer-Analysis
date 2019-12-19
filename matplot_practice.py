#%%
%matplotlib inline
#%%
# Import matplot library to create charts.
import matplotlib.pyplot as plt
import statistics
import numpy as np

#%%
# Set the x-axis to a list of strings for each month.
x_axis = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# Set the y-axis to a list of floats as the total fare in US dollars accumulated for each month.
y_axis = [10.02, 23.24, 39.20, 35.42, 32.34, 27.04, 43.82, 10.56, 11.85, 27.90, 20.71, 20.09]

#%%
# Create the plot
plt.plot(x_axis, y_axis)

# %%
# Create the plot with ax.plt()
fig, ax = plt.subplots()
ax.plot(x_axis, y_axis)

# %%
# Create the plot with ax.plt()
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(x_axis, y_axis)
# %%
# Create the plot with ax.plt()
ax = plt.axes()
ax.plot(x_axis, y_axis)

# %%
# Create the plot.
plt.plot(x_axis, y_axis)
plt.show()

# %%
# Create the plot and add a label for the legend.
plt.plot(x_axis, y_axis, label='Boston')
# Create labels for the x and y axes.
plt.xlabel("Date")
plt.ylabel("Fare($)")
# Set the y limit between 0 and 45.
plt.ylim(0, 45)
# Create a title.
plt.title("PyBer Fare by Month")
# Add the legend.
plt.legend()

# %%
# Create the plot.
plt.plot(x_axis, y_axis, marker="*", color="blue", linewidth=2, label='Boston')
# Create labels for the x and y axes.
plt.xlabel("Date")
plt.ylabel("Fare($)")
# Set the y limit between 0 and 45.
plt.ylim(0, 45)
# Create a title.
plt.title("PyBer Fare by Month")
# Add a grid.
plt.grid()
# Add the legend.
plt.legend()

# %%
# Create the plot with ax.plt()
fig, ax = plt.subplots()
ax.plot(x_axis, y_axis, marker="D", color="green", linewidth=2, label='Boston')
# Set a Title
ax.set_title("PyBer Fare by Month")
# Set Axis labels
ax.set_xlabel('Date')
ax.set_ylabel('Fare ($)')
# Set y-axis limit
ax.set_ylim(0, 45)
# Add a legend
ax.legend()
# Add gridlines
ax.grid()

# %%
# Create the plot
plt.bar(x_axis, y_axis)

# %%
# Create the plot.
plt.bar(x_axis, y_axis, color="green", label='Boston')
# Create labels for the x and y axes.
plt.xlabel("Date")
plt.ylabel("Fare($)")
# Create a title.
plt.title("PyBer Fare by Month")
# Add the legend.
plt.legend()

# %%
# Create the plot
plt.barh(x_axis, y_axis, color='magenta', label='Boston')
# Change the ticks in x-axis
plt.xticks(np.arange(0, 51, step=5.0))
# Orders the month from Jan to Dec
plt.gca().invert_yaxis()
# Add the legend.
plt.legend()
# Create labels for the x and y axes.
plt.xlabel("Date")
plt.ylabel("Fare($)")
# Create a title.
plt.title("PyBer Fare by Month")
# %%
# Create the plot with ax.plt()
fig, ax = plt.subplots()
ax.bar(x_axis, y_axis)

# %%
# Create the plot with ax.plt()
fig, ax = plt.subplots()
ax.barh(x_axis, y_axis, color='cyan', label='Chicago')
# Orders the month from Jan to Dec
ax.invert_yaxis()
# Add title
ax.set_title("PyBer Fare by Month")
# Set Axis labels
ax.set_xlabel('Date')
ax.set_ylabel('Fare ($)')
# Add a legend
ax.legend()

# %%
plt.plot(x_axis, y_axis, 'o')

# %%
plt.scatter(y_axis, x_axis, color = 'red', label='Chicago')
# Add legend
plt.legend()
# Add Title
plt.title("PyBer Fare by Month")
# axis labels
plt.xlabel("Date")
plt.ylabel("Fare($)")
# invert x axis
plt.gca().invert_yaxis()

# %%
#Creating bubble chart using list comprehension feature 
plt.scatter(x_axis, y_axis, s = [i * 3 for i in y_axis])

# %%
y_axis_larger = []
for data in y_axis:
  y_axis_larger.append(data*5)
fig, ax = plt.subplots()
ax.scatter(y_axis, x_axis,c='skyblue',linewidth='2',alpha=0.2, edgecolor='black',s= y_axis_larger)

# %%
#plt.pie(y_axis, labels=x_axis)
colors = ["slateblue", "magenta", "lightblue", "green", "yellowgreen", "greenyellow", "yellow", "orange", "gold", "indianred", "tomato", "mistyrose"]
explode_values = (0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0, 0, 0)
plt.subplots(figsize=(8, 8))
plt.pie(y_axis, explode=explode_values, labels=x_axis, colors= colors, autopct='%.1f%%')


# %%
# Calculate stdev for yxis to use in error bar
stdev_y_axis = statistics.stdev(y_axis)
#stdev_y_axis
#%%
plt.errorbar(x_axis, y_axis, yerr=stdev_y_axis, capsize=3)

# %%
plt.bar(x_axis, y_axis, yerr=stdev_y_axis, capsize=3)

# %%
