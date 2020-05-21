import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data.csv", delimiter=",")

time = data[0][2:] # time values in time.time() format
freq = data[1][2:] # also ignoring the first data entry

starting_point = time[0]
time = [point - starting_point for point in time] # making time start from 0

# Plotting the data
fig= plt.Figure()
plt.plot(time, freq)

# Set labels
plt.xlabel("time (s)")
plt.ylabel("Frequency diff (Hz)")
plt.title("Frequency change")

plt.grid()

#plt.show()
plt.savefig("test.png")

print("Done")
("Done")
