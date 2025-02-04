# Hands-on 3

```python
function x = fn(n) 
    x = 1;
    for i = 1:n
        for j = 1:n
            x = x + 1;
```
1. Time complexity of given function
    * `x = 1;` $T(n) = 1$
    * `for i = 1:n` $T(n) = n$
    * `for i = 1:n` $T(n) = \sum_{i=1}^{n-1} \sum_{j=1}^{n} 1$
    * `x = x + 1;` $T(n) = \sum_{i=1}^{n-1} \sum_{j=1}^{n-1} 1$
$T(n) = 1 + n^2$ and time complexity is $\theta(n^2)$

2. Plot
![Runtime of f(n) vs n](/runtime_plot.png)

3. Get time complexity for $\Omega$, $\theta$, and $O$
    * Lower Bound: For $n ≥ 1$, $T(n) ≥ n^2$, Therefore the lower bound is $\Omega(n^2)$
    * Upper Bound: $T(n) 1 + n^2 ≤ 2n^2, n ≥ 1$ Thus upper bound is $O(n^2)$
    * Given upper and lowerbound, we can get $\theta(n^2)$

