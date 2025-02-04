import time
import numpy as np
import matplotlib.pyplot as plt


def f(n):
    x = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x = x + 1
    return x


n_values = np.arange(10,10000,200)
times = []


for n in n_values:
    start = time.time()
    f(n)
    end = time.time()
    times.append(end - start)

n_values = np.array(n_values)
times = np.array(times)

coeffs = np.polyfit(n_values, times, 2)
poly_fit = np.poly1d(coeffs)

plt.figure(figsize=(10, 6))
plt.plot(n_values, times, 'bo', label='Timing data')
plt.plot(n_values, poly_fit(n_values), 'r-', label=f'Fitted quadratic')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Runtime of f(n) vs. n')
plt.legend()
plt.grid(True)
plt.show()
