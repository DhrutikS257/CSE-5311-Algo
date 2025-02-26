import numpy as np
import timeit, random

def generate_optimal_quicksort_array(arr: np.ndarray) -> np.ndarray:
    arr = np.array(arr)
    if arr.size <= 1:
        return arr
    mid = len(arr) // 2
    left = generate_optimal_quicksort_array(arr[:mid])
    right = generate_optimal_quicksort_array(arr[mid+1:])
    return np.concatenate((left, np.array([arr[mid]]), right))


def remove_nan(data: np.ndarray) -> np.ndarray:
    cleaned_rows = []
    for row in data:
        cleaned_row = row[~np.isnan(row)]
        cleaned_rows.append(cleaned_row)
    return np.array(cleaned_rows, dtype=object)

def read_data() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    best_case_data = np.genfromtxt('best_case.csv', delimiter=',')
    average_case_data = np.genfromtxt('average_case.csv', delimiter=',')
    worst_case_data = np.genfromtxt('worst_case.csv', delimiter=',')
    
    best_case_data = remove_nan(best_case_data.T)
    average_case_data = remove_nan(average_case_data.T)
    worst_case_data = remove_nan(worst_case_data.T)
    
    return best_case_data, average_case_data, worst_case_data

def random_partition(arr:np.ndarray, p:int, r:int):

    random.seed()

    i = random.randrange(p,r)

    arr[r], arr[i] = arr[i], arr[r]

    return partition(arr, p, r)

def partition(arr:np.ndarray, p:int, r:int) -> int:

    x = arr[r] 
    i = p - 1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]

    return i + 1

def random_q_sort(arr: np.ndarray, p: int, r: int) -> np.ndarray:
    if p < r:
        q = random_partition(arr, p, r)
        random_q_sort(arr, p, q - 1)
        random_q_sort(arr, q + 1, r)
    return arr

def quick_sort(arr: np.ndarray, p: int, r: int) -> np.ndarray:
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)
    return arr

def main():
    best_case_data, average_case_data, worst_case_data = read_data()

    for b_c, a_c, w_c in zip(best_case_data, average_case_data, worst_case_data):
        l = len(b_c)

        b_c_optimal = generate_optimal_quicksort_array(b_c)


        b_c_quick = b_c_optimal.copy()
        best_case_time = timeit.timeit(lambda: quick_sort(b_c_quick, 0, len(b_c_quick) - 1), number=1) * 1000


        b_c_random = b_c_optimal.copy()
        best_case_time_random = timeit.timeit(lambda: random_q_sort(b_c_random, 0, len(b_c_random) - 1), number=1) * 1000


        a_c_quick = a_c.copy()
        avg_case_time = timeit.timeit(lambda: quick_sort(a_c_quick, 0, len(a_c_quick) - 1), number=1) * 1000

        a_c_random = a_c.copy()
        avg_case_time_random = timeit.timeit(lambda: random_q_sort(a_c_random, 0, len(a_c_random) - 1), number=1) * 1000

        w_c_quick = w_c.copy()
        worst_case_time = timeit.timeit(lambda: quick_sort(w_c_quick, 0, len(w_c_quick) - 1), number=1) * 1000

        w_c_random = w_c.copy()
        worst_case_time_random = timeit.timeit(lambda: random_q_sort(w_c_random, 0, len(w_c_random) - 1), number=1) * 1000

        print(f"{'-'*60}")
        print(f"Data size: {l}")
        print(f"Best Case:")
        print(f"  Standard Quick Sort    : {best_case_time:.3f} ms")
        print(f"  Randomized Quick Sort  : {best_case_time_random:.3f} ms")
        print(f"Average Case:")
        print(f"  Standard Quick Sort    : {avg_case_time:.3f} ms")
        print(f"  Randomized Quick Sort  : {avg_case_time_random:.3f} ms")
        print(f"Worst Case:")
        print(f"  Standard Quick Sort    : {worst_case_time:.3f} ms")
        print(f"  Randomized Quick Sort  : {worst_case_time_random:.3f} ms\n")

if __name__ == "__main__":
    main()

