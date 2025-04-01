from helper import Node, print_ascii_tree
from typing import Optional
class BT:

    def __init__(self):
        self.root:Node = None
    
    def search(self, val:int) -> Node:
        x = self.root

        while x is not None:

            if val < x.val:
                x = x.left
            
            elif val > x.val:
                x = x.right
            
            else:
                return x
            
        return None
    
    def _minimum(self, node:Node) -> Node:

        while node.left is not None:
            node = node.left
        return node
    
    def _maximum(self, node:Node) -> Node:
        while node.right is not None:
            node = node.right
        return node

    def _search_last_node(self, val:int) -> Optional[Node]:
        n = self.root
        prev = None

        while n is not None:
            prev = n

            if val < n.val:
                n = n.left

            elif val > n.val:
                n = n.right
            
            else:
                return n

        return prev

    def insert(self, node:Node):
        prev_node = self._search_last_node(node.val)
        node.prev = prev_node

        if prev_node is None:
            self.root = node
        
        elif node.val < prev_node.val:
            prev_node.left = node

        else:
            prev_node.right = node

    def delete(self, val:int):
        n = self.search(val)

        if n is None:
            print(f"Node with value {val} not found")
            return


def run_test_from_file(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    bt = BT()

    for line in lines:
        parts = line.split()
        command = parts[0]

        if command == "insert":
            val = int(parts[1])
            bt.insert(Node(val = val))
            print(f"Inserted ({val})")

        elif command == "delete":
            val = int(parts[1])
            bt.delete(val)


        else:
            print(f"Unknown command: {line}")
    print("=== Binary Tree State ===")
    print_ascii_tree(bt.root)

if __name__ == "__main__":
    run_test_from_file("./tests/test1.txt")

