#%%
import matplotlib as ml
import pandas as pd
import re
#%%
#Merge two datasets
dataFile1='/Users/hebamaly/PyBer-Analysis/Livesession/bitcoin_cash_price.csv'
dataFile2='/Users/hebamaly/PyBer-Analysis/Livesession/dash_price.csv'

#%%
def cleanData(data: str) -> (int, None):
    cleanedData = re.findall("[0-9]+", data)
    out = ""
    for stuff in cleanedData:
        out = out + stuff
    if out != '':
        return int(out)
    else:
        return None
# %%
bitcoin_df=pd.read_csv(dataFile1)
dash_df=pd.read_csv(dataFile2)

# %%
clean_bitcoin_df=bitcoin_df.dropna(how='any')
clean_dash_df=dash_df.dropna(how='any')

# %%
clean_bitcoin_df['Market Cap'].apply(type)
clean_bitcoin_df['Market Cap'].astype(int)

# %%
clean_bitcoin_df['Market Cap'].apply(cleanData)
#%%
clean_bitcoin_df['Market Cap'].apply(type)
#%%
clean_bitcoin_df=clean_bitcoin_df.dropna(how='any')
#%%
clean_bitcoin_df['Market Cap'].astype(int)
# %%
# %%
clean_dash_df['Market Cap'].apply(cleanData)

# %%
clean_dash_df['Market Cap'].apply(type)

# %%
