#include "dynamic_array.hpp"
#include <cstddef>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream infile("test.txt");
    Array dynamic_array(2);
    string line;
    while (getline(infile, line)) {
        char* c_line = new char[line.size() + 1];
        strcpy(c_line, line.c_str());
        char* token0 = strtok(c_line, " ");

        if (strcmp(token0, "add") == 0) {
            char* token1 = strtok(NULL, " ");
            dynamic_array.add(atoi(token1));
        }
        else if (strcmp(token0, "delete") == 0) {
            int pop_val = dynamic_array.del();
            if(pop_val == -1) {
                cout << "Array is empty" << endl;
                continue;
            }
            cout << "Last element val: " << pop_val << endl;
        }
        else if (strcmp(token0, "print") == 0) {
            cout << "Array size: " << dynamic_array.length() << endl;
            cout << "Allocated array length: " << dynamic_array.get_total_allocated_length() << endl;
            cout << "Array: [ ";
            for (int i = 0; i < dynamic_array.length(); i++) {
                cout << dynamic_array.arr[i] << " ";
            }
            cout << "]" << endl;
        }
        delete[] c_line;
    }

    return 0;
}
