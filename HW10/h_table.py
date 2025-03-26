import math

def division_hash(key, table_size):
    return key % table_size

def multiplication_hash(key, table_size):
    A = 0.6180339887
    return math.floor(table_size * ((key * A) % 1))

class Node:

    def __init__(self, prev:'Node', key:int, value:int, next:'Node'):
        self.prev = prev
        self.key = key
        self.value = value
        self.next = next

class HashTable:

    def __init__(self, table_size:int, hash_func):
        self.table_size = table_size
        self.table = [None] * table_size
        self.hash_func = hash_func
        self.key_count = 0

    def insert(self, key, data):
        index = self.hash_func(key, self.table_size)
        if self.table[index] is None:
            self.table[index] = Node(None, key, data, None)
            self.key_count += 1
        else:
            node = self.table[index]
            while node.next is not None:
                node = node.next
            node.next = Node(node, key, data, None)
            self.key_count += 1

        self._check_and_resize()

    def search(self, key):
        index = self.hash_func(key, self.table_size)
        node = self.table[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def delete(self, key):
        index = self.hash_func(key, self.table_size)
        node = self.table[index]
        while node is not None:
            if node.key == key:
                if node.prev is None:
                    self.table[index] = node.next
                else:
                    node.prev.next = node.next
                self.key_count -= 1
                self._check_and_resize()
                return
            node = node.next


    def _check_and_resize(self):
        if self.key_count > self.table_size:
            self._resize_table(self.table_size * 2)

        elif self.key_count < self.table_size // 4:
            self._resize_table(self.table_size // 2)
        
    def _resize_table(self, new_size):
        
        print(f"Resizing table from {self.table_size} to {new_size}")
        new_table = [None] * new_size
        for node in self.table:
            while node is not None:
                index = self.hash_func(node.key, new_size)
                if new_table[index] is None:
                    new_table[index] = Node(None, node.key, node.value, None)
                else:
                    new_node = new_table[index]
                    while new_node.next is not None:
                        new_node = new_node.next
                    new_node.next = Node(new_node, node.key, node.value, None)
                node = node.next
        self.table = new_table
        self.table_size = new_size

    def display(self):
        print("=== Hash Table State ===")
        for i, node in enumerate(self.table):
            print(f"Bucket {i}:", end=" ")
            current = node
            while current:
                print(f"({current.key}: {current.value})", end=" <-> ")
                current = current.next
            print("None")
        print("========================")


def run_test_from_file(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    hash_func = None
    table_size = None
    ht = None

    for line in lines:
        parts = line.split()
        command = parts[0]

        if command == "hash_func":
            if parts[1] == "division":
                hash_func = division_hash
            elif parts[1] == "multiplication":
                hash_func = multiplication_hash
            else:
                raise ValueError("Unknown hash function")

        elif command == "table_size":
            table_size = int(parts[1])
            if hash_func is None:
                raise ValueError("Hash function must be defined before setting table size")
            ht = HashTable(table_size, hash_func)

        elif command == "insert":
            key, val = int(parts[1]), int(parts[2])
            ht.insert(key, val)
            print(f"Inserted ({key}: {val})")
            ht.display()

        elif command == "search":
            key = int(parts[1])
            result = ht.search(key)
            print(f"Search for key {key}: {'Found: ' + str(result) if result is not None else 'Not Found'}")

        elif command == "delete":
            key = int(parts[1])
            ht.delete(key)
            print(f"Deleted key {key}")
            ht.display()

        else:
            print(f"Unknown command: {line}")


if __name__ == "__main__":
    run_test_from_file("./tests/test_case_10_large.txt")




