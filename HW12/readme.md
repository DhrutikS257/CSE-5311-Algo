# HW12

### How to run the code:
```bash
docker compose up --build
```
---
### Given a dynamic table that doubles in size when it needs more space. Find the amortized runtime for inserting n elements.
Aggregate Method: We know that the insertions are $O(1)$ if the table doesn't need to be resized. But it would be $O(n)$, meaning allocating spacing is constant but copying data is linear.
Since resize doesn't happen every operation we can say that the amortized runtime is $O(1)$.

Accounting Method: 
- Assumption:
  - Table starts with size 1
  - It doubles everytime it get full
  - Perform n insertions
- Each insertion:
  - Insertion cost: 1
  - Resize cost: 2
- During resize:
  - Resize array by 2*k
  - Copy k elements
  - This one operation saved k resizes
Most of the time insertion cost 1, but sometimes it could cost 3 if resize need to be done. Calculating the total for n operations it would be less than 3n, amortized complexity is $O(1)$.
