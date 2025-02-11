# HW4

## Proving Time Complexity
* Problem 1: $O(n * k)$, since `merge()` takes $O(n)$ where n is the length of arr1 + arr2. Since we will be merging k arrays, it run `merge()` k amount of times. 
* Problem 2: $O(n)$, since we are iterating through an array which is already sorted and only appending variables in new array that are now set to curNum which keeps tracks of duplicate. 

## Improvement
* Problem 1: We can use min heap to keep track of obtaining minimum element from given k arrays, and getting the min value take $O(log(k))$ and we will be doing this n time there for our time complexity will be $O(n * log(k))$ which will less than $O(n * k)$
* Problem 2: We can use sets, this wouldn't change the time complexity, but if the array is unsorted the function would still function in $O(n)$