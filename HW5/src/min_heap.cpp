#include <iostream> 
#include <vector>

using namespace std;

int parent(int i ) {
    return (i-1)/2;
}

int left(int i) {
    return 2*i;
}

int right(int i) {
    return 2*i + 1;
}

struct node
{
    int key;
    int data;
};


void min_heapify(vector<int>& arr, int i) {
    int smallest;
    int l = left(i);
    int r = right(i);

    if (l <= arr.size() && arr[l] < arr[i])
        smallest = l;
    else
        smallest = i;
    
    if (r <= arr.size() && arr[r] < arr[smallest])
        smallest = r;
    
    if (smallest != i) {
        swap(arr[i], arr[smallest]);
        min_heapify(arr, smallest);
    }
}

vector<node> build_nodes(vector<int>& arr) {
    vector<node> nodes;
    for (int i = 0; i < arr.size(); i++) {
        node n;
        n.key = arr[i];
        n.data = arr[i];
        nodes.push_back(n);
    }
    return nodes;
}

vector<node> build_min_heap(vector<node>& arr){
    
}


int main() {
    vector<int> arr1 = {27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0};

    cout << "Original array: ";
    for (int i = 0; i < arr1.size(); i++)
        cout << arr1[i] << " ";

    for (int i = arr1.size()/2; i >= 0; i--)
        min_heapify(arr1, i);

    cout << "\nMin-Heap after heapify operation: ";
    for (int i = 0; i < arr1.size(); i++)
        cout << arr1[i] << " ";

    return 0;
}