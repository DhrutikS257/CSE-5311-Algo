#include "bubble_sort.hpp"
#include <iostream>
using namespace std;

#define SWAP(a, b) { uint32_t temp = a; a = b; b = temp; }

void print(uint32_t *arr, int size) {
    for(int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void bubbleSort(uint32_t *arr, int size) {
    for(int i = 1; i < size; i++) {
        for(int j = 0; j < size - 1; j++) {
            if (arr[j] > arr[j+1]) {
                SWAP(arr[j],arr[j+1])
            }
        }
    }
}




