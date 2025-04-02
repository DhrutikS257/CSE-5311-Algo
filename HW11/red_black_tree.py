from helper import print_ascii_tree, RedBlackNode as Node
from typing import Optional

class RedBlackTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def left_rotate(self, x: Node):
        y = x.right
        if y is None:
            return 
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

    def right_rotate(self, y: Node):
        x = y.left
        if x is None:
            return 
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

    def insert(self, val: int):
        new_node = Node(val)
        parent = None
        current = self.root

        while current is not None:
            parent = current
            if new_node.val < current.val:
                current = current.left
            else:
                current = current.right

        new_node.prev = parent
        if parent is None:

            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix the red-black properties.
        self.insert_fixup(new_node)

    def insert_fixup(self, z: Node):
        while z.prev is not None and getattr(z.prev, 'red', False):
            if z.prev == z.prev.prev.left:
                y = z.prev.prev.right  # uncle
                if y is not None and getattr(y, 'red', False):
                    # Case 1: uncle is red.
                    z.prev.red = False
                    y.red = False
                    z.prev.prev.red = True
                    z = z.prev.prev
                else:
                    if z == z.prev.right:

                        z = z.prev
                        self.left_rotate(z)

                    z.prev.red = False
                    z.prev.prev.red = True
                    self.right_rotate(z.prev.prev)
            else:

                y = z.prev.prev.left 
                if y is not None and getattr(y, 'red', False):

                    z.prev.red = False
                    y.red = False
                    z.prev.prev.red = True
                    z = z.prev.prev
                else:
                    if z == z.prev.left:

                        z = z.prev
                        self.right_rotate(z)

                    z.prev.red = False
                    z.prev.prev.red = True
                    self.left_rotate(z.prev.prev)

        if self.root is not None:
            self.root.red = False

    def search(self, val: int) -> Optional[Node]:
        current = self.root
        while current is not None:
            if val == current.val:
                return current
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return None

    def minimum(self, node: Node) -> Node:
        while node.left is not None:
            node = node.left
        return node

    def transplant(self, u: Node, v: Optional[Node]):
        if u.prev is None:
            self.root = v
        elif u == u.prev.left:
            u.prev.left = v
        else:
            u.prev.right = v
        if v is not None:
            v.prev = u.prev

    def delete(self, val: int):

        z = self.search(val)
        if z is None:
            print(f"Value {val} not found in the tree.")
            return

        self.delete_node(z)

    def delete_node(self, z: Node):
        y = z
        y_original_color = y.red  
        if z.left is None:
            x = z.right
            self.transplant(z, z.right)
        elif z.right is None:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.red
            x = y.right
            if y.prev == z:
                if x is not None:
                    x.prev = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                if y.right is not None:
                    y.right.prev = y
            self.transplant(z, y)
            y.left = z.left
            if y.left is not None:
                y.left.prev = y

            y.red = z.red


        if not y_original_color:
            self.delete_fixup(x)

    def delete_fixup(self, x: Optional[Node]):
        while x != self.root and (x is None or not x.red):
            if x is not None and x.prev is not None and x == x.prev.left:
                w = x.prev.right  
                if w is not None and w.red:

                    w.red = False
                    x.prev.red = True
                    self.left_rotate(x.prev)
                    w = x.prev.right
                if (w.left is None or not w.left.red) and (w.right is None or not w.right.red):

                    if w is not None:
                        w.red = True
                    x = x.prev
                else:
                    if w.right is None or not w.right.red:

                        if w.left is not None:
                            w.left.red = False
                        w.red = True
                        self.right_rotate(w)
                        w = x.prev.right

                    w.red = x.prev.red
                    x.prev.red = False
                    if w.right is not None:
                        w.right.red = False
                    self.left_rotate(x.prev)
                    x = self.root
            else:

                if x is not None and x.prev is not None:
                    w = x.prev.left 
                    if w is not None and w.red:

                        w.red = False
                        x.prev.red = True
                        self.right_rotate(x.prev)
                        w = x.prev.left
                    if (w.right is None or not w.right.red) and (w.left is None or not w.left.red):

                        if w is not None:
                            w.red = True
                        x = x.prev
                    else:
                        if w.left is None or not w.left.red:

                            if w.right is not None:
                                w.right.red = False
                            w.red = True
                            self.left_rotate(w)
                            w = x.prev.left

                        w.red = x.prev.red
                        x.prev.red = False
                        if w.left is not None:
                            w.left.red = False
                        self.right_rotate(x.prev)
                        x = self.root
                else:

                    break
        if x is not None:
            x.red = False


def run_test_from_file(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    r_b_t = RedBlackTree()

    for line in lines:
        parts = line.split()
        command = parts[0]

        if command == "insert":
            val = int(parts[1])
            r_b_t.insert(val)
            print(f"Inserted ({val})")

        elif command == "delete":
            val = int(parts[1])
            r_b_t.delete(val)
            print(f"Deleted ({val})")


        else:
            print(f"Unknown command: {line}")
    print("\n=== Binary Tree State ===")
    print_ascii_tree(r_b_t.root)

if __name__ == "__main__":
    run_test_from_file("./tests/test1.txt")
