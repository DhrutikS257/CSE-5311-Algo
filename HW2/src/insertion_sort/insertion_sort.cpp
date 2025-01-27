#include "insertion_sort.hpp"
#include <iostream>
using namespace std;

#define SWAP(a, b) { uint32_t temp = a; a = b; b = temp; }

void print(uint32_t *arr, int size) {
    for(int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void insertionSort(uint32_t *arr, int size) {
    for(int i = 1; i < size; i++) {
        int j = i - 1;
        while(j >= 0 && arr[j] > arr[i]) {
            SWAP(arr[j],arr[i]);
            i--;
            j--;
        }
    }
}


