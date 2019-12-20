# %%
import numpy
import statistics

# %%
dataSet = [3,3,4,5,5,6,7,7,8,9]
median = 6
lowerquartile = 4
upperquartile = 8
IQR = upperquartile - lowerquartile
# %%
def getmedian(dataSet: list)-> int:
    medianordinal: int = len(dataSet)/2
    return dataSet(medianordinal)
    
# %%
