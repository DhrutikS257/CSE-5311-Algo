#include "selection_sort.hpp"
#include <iostream>
using namespace std;

void benchmarkInsertion() {

    uint32_t arr[] = {42, 7, 23, 91, 5, 15, 67, 38, 10, 3};
    int size = sizeof(arr) / sizeof(*arr);

    cout << "Selection Sort (Before): ";
    print(arr, size);

    selectionSort(arr, size);
    cout << "Selection Sort (After): ";
    print(arr, size);
}

int main() {
    benchmarkInsertion();
    return 0;
}