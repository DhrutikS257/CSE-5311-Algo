import time
import numpy as np
import matplotlib.pyplot as plt

# Define the function f(n) in Python
def f(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x = x + 1
    return x

# Choose a range of n values.
# For demonstration, we will use a range that shows the quadratic behavior.
n_values = np.arange(10,10000,200)# 20 values from 100 to 2000
times = []

# Time the function for each n
for n in n_values:
    start = time.time()
    f(n)
    end = time.time()
    times.append(end - start)

# Convert to numpy arrays for fitting
n_values = np.array(n_values)
times = np.array(times)

# Fit a quadratic polynomial to the timing data
coeffs = np.polyfit(n_values, times, 2)
poly_fit = np.poly1d(coeffs)

# Plot the data and the fitted curve
plt.figure(figsize=(10, 6))
plt.plot(n_values, times, 'bo', label='Timing data')
plt.plot(n_values, poly_fit(n_values), 'r-', label=f'Fitted quadratic')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Runtime of f(n) vs. n')
plt.legend()
plt.grid(True)
plt.show()
