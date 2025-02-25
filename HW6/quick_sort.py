import numpy as np
import timeit

def remove_nan(data: np.ndarray) -> np.ndarray:
    cleaned_rows = []
    for row in data:
        cleaned_row = row[~np.isnan(row)]
        cleaned_rows.append(cleaned_row)
    return np.array(cleaned_rows, dtype=object)

def partition(array, low, high):

    return 

def quick_sort(array, low, high):

    if low < high:

        part = partition(array, low, high)

        # quick_sort(array, low, part - 1)

        # quick_sort(array, part + 1, high)


def read_data() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    best_case_data = np.genfromtxt('best_case.csv', delimiter=',')
    average_case_data = np.genfromtxt('average_case.csv', delimiter=',')
    worst_case_data = np.genfromtxt('worst_case.csv', delimiter=',')
    
    best_case_data = remove_nan(best_case_data.T)
    average_case_data = remove_nan(average_case_data.T)
    worst_case_data = remove_nan(worst_case_data.T)
    
    return best_case_data, average_case_data, worst_case_data

def main():
    best_case_data, average_case_data, worst_case_data = read_data()

    sorted_best_case, sorted_average_case, sorted_worst_case = [], [], []

    for b_c, a_c, w_c in zip(best_case_data, average_case_data, worst_case_data):

        s_b_c = timeit.default_timer()
        sorted_best_case.append(quick_sort(b_c, 0, len(b_c) - 1))
        print(f"Best Case Time for size {len(b_c)} is {timeit.default_timer() - s_b_c}")

        s_a_c = timeit.default_timer()
        sorted_average_case.append(quick_sort(a_c, 0, len(a_c) - 1))
        print(f"Average Case Time for size {len(a_c)} is {timeit.default_timer() - s_a_c}")

        s_w_c = timeit.default_timer()
        sorted_worst_case.append(quick_sort(w_c, 0, len(w_c) - 1))
        print(f"Worst Case Time for size {len(w_c)} is {timeit.default_timer() - s_w_c}")


if __name__ == "__main__":
    main()