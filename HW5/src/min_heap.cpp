#include <iostream>
#include <vector>

using namespace std;
int parent(int i) {
    return (i - 1) >> 1;
}


int left(int i) {
    return (i << 1) + 1;
}

int right(int i) {
    return (i << 1) + 2;
}


template <typename T>
void min_heapify(vector<T>& heap, int i, int n) {
    int l = left(i);
    int r = right(i);
    int smallest = i;

    if (l < n && heap[l] < heap[smallest])
        smallest = l;
    if (r < n && heap[r] < heap[smallest])
        smallest = r;
    if (smallest != i) {
        swap(heap[i], heap[smallest]);
        min_heapify(heap, smallest, n);
    }
}


template <typename T>
void build_min_heap(vector<T>& heap) {
    int n = heap.size();

    for (int i = parent(n - 1); i >= 0; --i) {
        min_heapify(heap, i, n);
    }
}


template <typename T>
T top_heap(const vector<T>& heap) {
    if (heap.empty())
        throw runtime_error("Heap is empty");
    return heap.front();
}

template <typename T>
T pop_heap(vector<T>& heap) {
    if (heap.empty())
        throw runtime_error("Heap is empty");
    T root = heap.front();
    heap.front() = heap.back();
    heap.pop_back();
    min_heapify(heap, 0, heap.size());
    return root;
}


template <typename T>
void print_heap(const vector<T>& heap) {
    for (const auto& item : heap)
        cout << item << " ";
    cout << "\n";
}

int main() {

    vector<int> data = {27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0};

    cout << "Original array: ";
    for (int d : data)
        cout << d << " ";
    cout << "\n";


    build_min_heap(data);
    cout << "Heap array after build_min_heap(): ";
    print_heap(data);


    cout << "\nRemoving elements from the heap:\n";
    while (!data.empty()) {
        try {
            int top = top_heap(data);
            cout << "Top element: " << top << "\n";
            int popped = pop_heap(data);
            cout << "Popped element: " << popped << "\n";
            cout << "Heap now: ";
            print_heap(data);
        } catch (const runtime_error& e) {
            cout << "Heap is empty!\n";
            break;
        }
    }

    return 0;
}
