from typing import Optional
from helper import Node, print_ascii_tree

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, node:Node):
        y = None
        x = self.root
        while x is not None:
            y = x
            if node.val < x.val:
                x = x.left

            else:
                x = x.right
        node.prev = y

        if y is None:
            self.root = node

        elif node.val < y.val:
            y.left = node

        else:
            y.right = node

    def _minimum(self, node:Node) -> Node:
        while node.left is not None:
            node = node.left
        return node

    def _maximum(self, node:Node) -> Node:
        while node.right is not None:
            node = node.right
        return node


    def _transplant(self, u: Node, v:Node):
        if u.prev is None:
            self.root = v

        elif u == u.prev.left:
            u.prev.left = v

        else:
            u.prev.right = v

        if v is not None:
            v.prev = u.prev

    def delete(self, node:Node):

        if node.left is None:
            self._transplant(node,node.right)

        elif node.right is None:
            self._transplant(node,node.left)

        else:
            y = self._minimum(node.right)

            if y.prev != node:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.prev = y

            self._transplant(node, y)
            y.left = node.left
            y.left.prev = y

    def search(self, val:int) -> Optional[Node]:
        x = self.root
        while x is not None:
            if val < x.val:
                x = x.left
            elif val > x.val:
                x = x.right
            else:
                return x
        return None




def run_test_from_file(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    bt = BinaryTree()

    for line in lines:
        parts = line.split()
        command = parts[0]

        if command == "insert":
            val = int(parts[1])
            bt.insert(Node(val = val))
            print(f"Inserted ({val})")

        elif command == "delete":
            val = int(parts[1])
            # Find the node to delete
            node_to_delete = bt.search(val)
            if node_to_delete is None:
                print(f"Node with value {val} not found")
                continue
            else:
                bt.delete(node_to_delete)
                print(f"Deleted ({val})")


        else:
            print(f"Unknown command: {line}")
    print("=== Binary Tree State ===")
    print_ascii_tree(bt.root)

if __name__ == "__main__":
    run_test_from_file("./tests/test1.txt")
