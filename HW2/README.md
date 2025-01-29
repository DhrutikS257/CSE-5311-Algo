# Sorting Algos

### Program Details

```
C++ version: 14.2.0
How to run the program: docker compose up --build
```

### Argue selection sort correctness
```
Loop invariant: A[0...i-1]
Initialization: A[0:-1] is empty, so loop invariant holds true
Maintenance: 
    - Find the smallest element (A[i:n-1])
    - Swap the smallest element with A[i]
Since we are swapping with A[i] it will have the smallest element from A[i:] therefore A[i+1:n-1] is unsorted
Termination:
Outer loops terminates when i = n - 2, since A[n-1] is already sorted and is the max num from the array. Therefore when loop finished array from A[0:i-1] is sorted
```

### Benchmark 
```
OS: MacOS
CPU: M2 Pro
RAM: 16GB
```
![Graph](/HW2/algo-graph.png)
