#include <iostream> 
#include <vector>

using namespace std;

vector<int> removeDuplicate(vector<int>* arr) {
    vector<int> result;
    uint curNum;

    for(auto &num: *arr) {

        if (curNum && curNum != num) {
            result.push_back(num);
            curNum = num;
        } 
        else if(!curNum) {
            result.push_back(num);
            curNum = num;
        }
    }
    return result;
}

void printArray(vector<int>* arr) {
    cout << "Remove Duplicate Result = [ ";
    for(auto &num : *arr) {
        cout << num << " ";
    }
    cout << "]" << endl;
}

int main() {
    vector<int> a_1 = {2, 2, 2, 2, 2};
    vector<int> a_2 = {1, 2, 2, 3, 4, 4, 4, 5, 5};

    vector<int> r_1 = removeDuplicate(&a_1);
    printArray(&r_1);
    vector<int> r_2 = removeDuplicate(&a_2);
    printArray(&r_2);
    return 0;
}