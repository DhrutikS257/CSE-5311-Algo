#ifndef DYNAMIC_ARRAY_HPP
#define DYNAMIC_ARRAY_HPP
#include <cstdlib>
class Array {
    public:
        int *arr;
        Array(int length){
            arr = (int*)calloc(--length, sizeof(int));
            total_array_length = length;
        }
        void add(int value) {
            if(last_elem_ind >= total_array_length) {
                resize();
            }
            arr[++last_elem_ind] = value;
        }
        int del(){
            if(last_elem_ind > 0) {
                return arr[last_elem_ind--];
            }
            return -1;
        }
        int length(){
            return last_elem_ind + 1;
        }
        ~Array(){
            free(arr);
        }

        int get_total_allocated_length() {
            return total_array_length;
        }

    private:
        int total_array_length;
        int last_elem_ind = -1;
        void resize() {
            total_array_length *= 2;
            int* temp = (int*)realloc(arr, total_array_length * sizeof(int));
            arr = temp;
        }

};

#endif
