# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
datafile = '/Users/hebamaly/PyBer-Analysis/Live session2/avg_rain_state.csv'

# %%
rain_df = pd.read_csv(datafile)

# %%
x_axis = np.arange(len(rain_df))

# %%
