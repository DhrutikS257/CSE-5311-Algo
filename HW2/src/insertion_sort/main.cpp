#include "insertion_sort.hpp"
#include <iostream>
#include <chrono>
using namespace std;
using namespace chrono;
int main() {
    uint32_t arr[] = {42, 7, 23, 91, 5, 15, 67, 38, 10, 3};
    int size = sizeof(arr) / sizeof(*arr);

    cout << "Selection Sort (Before): ";
    print(arr, size);

    high_resolution_clock::time_point start = std::chrono::high_resolution_clock::now();
    insertionSort(arr, size);
    high_resolution_clock::time_point end = std::chrono::high_resolution_clock::now();
    duration<double, std::milli> duration = end - start;
    cout << "Selection Sort (After): ";
    print(arr, size);
    cout << "Time taken: " << duration.count() << " ms" << endl;
    return 0;
}