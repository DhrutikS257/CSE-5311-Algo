from typing import Optional
from helper import AVLNode as Node, print_ascii_tree
class AVLTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def get_height(self, node: Optional[Node]) -> int:
        if not node:
            return 0
        return node.height

    def update_height(self, node: Node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node: Node) -> int:
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, x: Node) -> Node:
        y = x.right
        if y is None:
            return x
        x.right = y.left
        if y.left is not None:
            y.left.prev = x
        y.prev = x.prev
        if x.prev is None:
            self.root = y
        elif x == x.prev.left:
            x.prev.left = y
        else:
            x.prev.right = y
        y.left = x
        x.prev = y
        self.update_height(x)
        self.update_height(y)
        return y

    def right_rotate(self, y: Node) -> Node:
        x = y.left
        if x is None:
            return y
        y.left = x.right
        if x.right is not None:
            x.right.prev = y
        x.prev = y.prev
        if y.prev is None:
            self.root = x
        elif y == y.prev.right:
            y.prev.right = x
        else:
            y.prev.left = x
        x.right = y
        y.prev = x
        self.update_height(y)
        self.update_height(x)
        return x

    def rebalance(self, node: Node) -> Node:
        self.update_height(node)
        balance = self.get_balance(node)
        if balance > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def insert(self, val: int):
        self.root = self._insert(self.root, val, None)

    def _insert(self, node: Optional[Node], val: int, prev: Optional[Node]) -> Node:
        if node is None:
            new_node = Node(val)
            new_node.prev = prev
            return new_node
        if val < node.val:
            node.left = self._insert(node.left, val, node)
        else:
            node.right = self._insert(node.right, val, node)
        return self.rebalance(node)

    def min_value_node(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, val: int):
        def _delete(node: Optional[Node], val: int) -> Optional[Node]:
            if node is None:
                return node
            if val < node.val:
                node.left = _delete(node.left, val)
            elif val > node.val:
                node.right = _delete(node.right, val)
            else:
                if node.left is None:
                    temp = node.right
                    if temp:
                        temp.prev = node.prev
                    node = None
                    return temp
                elif node.right is None:
                    temp = node.left
                    if temp:
                        temp.prev = node.prev
                    node = None
                    return temp
                temp = self.min_value_node(node.right)
                node.val = temp.val
                node.right = _delete(node.right, temp.val)
            if node is None:
                return node
            return self.rebalance(node)
    
        self.root = _delete(self.root, val)

def run_test_from_file(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    bt = AVLTree()

    for line in lines:
        parts = line.split()
        command = parts[0]

        if command == "insert":
            val = int(parts[1])
            bt.insert(val)
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


