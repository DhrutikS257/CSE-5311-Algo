import matplotlib.pyplot as plt

# Data derived from your log output:
sizes = [5, 10, 20, 50, 100, 200, 500]

# Standard Quick Sort times in milliseconds:
best_times   = [0.012, 0.014, 0.045, 0.254, 1.059, 4.284, 26.942]
avg_times    = [0.002, 0.007, 0.016, 0.050, 0.120, 0.274, 0.817]
worst_times  = [0.003, 0.011, 0.031, 0.183, 0.687, 2.653, 18.087]

plt.figure(figsize=(10, 6))
plt.plot(sizes, best_times, marker='o', label='Best Case')
plt.plot(sizes, avg_times, marker='o', label='Average Case')
plt.plot(sizes, worst_times, marker='o', label='Worst Case')

plt.xlabel('Data Size')
plt.ylabel('Time (ms)')
plt.title('Standard Quick Sort Execution Times')
plt.legend()

plt.savefig("quick_sort_times.png")