from matplotlib import pyplot as plt
import timeit

def func(n):
    x = 1
    for i in range(1,n):
        for j in range(1,n):
            j += 1

def plot():
    time = []
    n = []
    for i in range(1,1000):
        start = timeit.default_timer()
        func(i)
        end = timeit.default_timer()
        time.append(end-start)
        n.append(i)
    
    plt.plot(n,time)
    plt.xlabel('n')
    plt.ylabel('time')
    plt.title('Time Complexity')
    plt.show()


plot()