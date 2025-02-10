#include <iostream> 
#include <vector>

using namespace std;

vector<int> merge(vector<int>* a_1, vector<int>* a_2) {
    vector<int> result;
    uint8_t i = 0;
    uint8_t j = 0;

    while (i < a_1->size() || j < a_2->size()) {
        if (i < a_1->size() && j < a_2->size()) {
            if (a_1->at(i) < a_2->at(j)) {
                result.push_back(a_1->at(i));
                i++;
            }
            else {
                result.push_back(a_2->at(j));
                j++;
            }
        }
        else if(i < a_1->size()) {
            result.push_back(a_1->at(i));
            i++;
        }
        else {
            result.push_back(a_2->at(j));
            j++;
        }
    }
    return result;
}

void printArray(vector<int>* arr) {
    cout << "Merge Result = [ ";
    for(auto &num : *arr) {
        cout << num << " ";
    }
    cout << "]" << endl;
}

int main() {
    vector<int> a_1 = {1, 3, 5, 7};
    vector<int> a_2 = {2, 4, 6, 8};
    vector<int> a_3 = {0, 9, 10, 11};


    vector<int> temp = merge(&a_1, &a_2);
    vector<int> r_1 = merge(&temp, &a_3);

    printArray(&r_1);

    vector<int> a_4 = {1, 3, 7};
    vector<int> a_5 = {2, 4, 8};
    vector<int> a_6 = {9, 10, 11};

    vector<int> temp_2 = merge(&a_4, &a_5);
    vector<int> r_2 = merge(&temp_2, &a_6);

    printArray(&r_2);

    return 0;
}