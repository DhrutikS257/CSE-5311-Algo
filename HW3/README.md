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

2. Plot

