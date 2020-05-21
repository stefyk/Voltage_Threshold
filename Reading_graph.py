import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("data.csv", delimiter=",")

time = data[0][2:] # time values in time.time() format
freq = data[1][2:] # also ignoring the first data entry

starting_point = time[0]
time = [point - starting_point for point in time] # making time start from 0

# Plotting the data
fig, ax = plt.subplots()
ax.plot(time, freq)


# Set labels
ax.set(xlabel='time (s)', ylabel='Frequency diff (Hz)',
       title='Frequency change')
ax.grid()

fig.savefig("Frequency.png")
plt.show()

print("Done")
