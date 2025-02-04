import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def f(n):
    x = 1
    y = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            x = x + 1
            y = i + j
    return x


n_values = np.arange(10,10000,500)
times = []


for n in n_values:
    start = time.time()
    f(n)
    end = time.time()
    times.append(end - start)


def poly_fit(x, a, b, c):
    return a*x**2 + b*x + c

popt, pcov = curve_fit(poly_fit, n_values, times)

plt.figure(figsize=(10, 6))
plt.plot(n_values, times, 'bo', label='Timing data')
plt.plot(n_values, poly_fit(n_values, *popt), 'r-', label='Fitted quadratic')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Runtime of f(n) vs. n')
plt.legend()
plt.grid(True)
plt.show()
