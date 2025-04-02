from helper import BTNode as Node, print_ascii_tree
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

    def _transplant(self, u:Node, v:Node):
        if u.prev is None:
            self.root = v

        elif u == u.prev.left:
            u.prev.left = v

        else:
            u.prev.right = v

        if v is not None:
            v.prev = u.prev

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
        
        # Check if the node exists before attempting to delete it
        if n is None:
            return
            
        if n.left == None:
            self._transplant(n, n.right)

        elif n.right == None:
            self._transplant(n, n.left)

        else:
            y = self._minimum(n.right)
            if y.prev != n:
                self._transplant(y, y.right)
                y.right = n.right
                y.right.prev = y
            self._transplant(n, y)
            y.left = n.left
            y.left.prev = y


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
            print(f"Deleted ({val})")


        else:
            print(f"Unknown command: {line}")
    print("\n=== Binary Tree State ===")
    print_ascii_tree(bt.root)

if __name__ == "__main__":
    run_test_from_file("./tests/test1.txt")

