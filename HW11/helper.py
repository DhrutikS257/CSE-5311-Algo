from typing import Optional
class BTNode:

    def __init__(self, val: int, left: Optional['BTNode'] = None, right: Optional['BTNode'] = None, prev: Optional['BTNode'] = None):
        self.val = val
        self.left = left
        self.right = right
        self.prev = prev

class RedBlackNode(BTNode):

    def __init__(self, val, left = None, right = None, prev = None):
        super().__init__(val, left, right, prev)
        self.red = True

class AVLNode(BTNode):
    def __init__(self, val: int, left: Optional['AVLNode'] = None, right: Optional['AVLNode'] = None, parent: Optional['AVLNode'] = None):
        super().__init__(val, left, right, parent)
        self.height = 1


def print_ascii_tree(root: Optional[BTNode]):

    def _display_aux(node):
        # Returns a tuple: (list_of_lines, width, height, horizontal_root_position)
        # Convert node value and its color.
        if hasattr(node, 'red'):
            s = f"{node.val}{'(R)' if node.red else '(B)'}"
        else:
            s = str(node.val)

        # Leaf node.
        if node.left is None and node.right is None:
            width = len(s)
            height = 1
            middle = width // 2
            return [s], width, height, middle

        # Only left child.
        if node.right is None:
            left_lines, left_w, left_h, left_mid = _display_aux(node.left)
            first_line = (left_mid + 1) * " " + (left_w - left_mid - 1) * "_" + s
            second_line = left_mid * " " + "/" + (left_w - left_mid - 1 + len(s)) * " "
            shifted_left = [line + " " * len(s) for line in left_lines]
            return [first_line, second_line] + shifted_left, left_w + len(s), left_h + 2, left_w + len(s) // 2

        # Only right child.
        if node.left is None:
            right_lines, right_w, right_h, right_mid = _display_aux(node.right)
            first_line = s + right_mid * "_" + (right_w - right_mid) * " "
            second_line = (len(s) + right_mid) * " " + "\\" + (right_w - right_mid - 1) * " "
            shifted_right = [" " * len(s) + line for line in right_lines]
            return [first_line, second_line] + shifted_right, right_w + len(s), right_h + 2, len(s) // 2

        # Two children.
        left_lines, left_w, left_h, left_mid = _display_aux(node.left)
        right_lines, right_w, right_h, right_mid = _display_aux(node.right)
        first_line = (left_mid + 1) * " " + (left_w - left_mid - 1) * "_" + s + right_mid * "_" + (right_w - right_mid) * " "
        second_line = left_mid * " " + "/" + (left_w - left_mid - 1 + len(s) + right_mid) * " " + "\\" + (right_w - right_mid - 1) * " "
        if left_h < right_h:
            left_lines += [" " * left_w] * (right_h - left_h)
        elif right_h < left_h:
            right_lines += [" " * right_w] * (left_h - right_h)
        merged_lines = [l + " " * len(s) + r for l, r in zip(left_lines, right_lines)]
        return [first_line, second_line] + merged_lines, left_w + right_w + len(s), max(left_h, right_h) + 2, left_w + len(s) // 2

    if root is None:
        print("The tree is empty.")
        return
    lines, _, _, _ = _display_aux(root)
    for line in lines:
        print(line)
