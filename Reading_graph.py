import numpy as np

csv = np.genfromtxt("Change in Frequency over time.csv", delimiter= ",")
freq_data= csv [:,1]
print (freq_data)