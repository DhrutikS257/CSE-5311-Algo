#include "selection_sort.hpp"
#include <iostream>
using namespace std;

#define SWAP(a, b) { uint32_t temp = a; a = b; b = temp; }

void print(uint32_t *arr, int size) {
    for(int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void selectionSort(uint32_t *arr, int size) {
    for(int i = 0; i < size; i++) {
        int curMin = i;

        for(int j = i+1; j < size; j++) {
            if(arr[j] < arr[curMin]) 
                curMin = j;
        }
        
        if(curMin != i)
            SWAP(arr[i],arr[curMin]);
    }
}




