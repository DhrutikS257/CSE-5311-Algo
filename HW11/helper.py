from typing import Optional
class Node:

    def __init__(self, val: int, left: Optional['Node'] = None, right: Optional['Node'] = None, prev: Optional['Node'] = None):
        self.val = val
        self.left = left
        self.right = right
        self.prev = prev

def print_ascii_tree(root: Optional[Node]):
        """
        Prints the binary tree in an ASCII art style.
        """
        def _display_aux(node):
            # Returns a tuple: (list_of_lines, width, height, horizontal_root_position)
            if node.left is None and node.right is None:
                line = str(node.val)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            if node.right is None:
                # Only left child.
                left_lines, left_w, left_h, left_mid = _display_aux(node.left)
                s = str(node.val)
                u = len(s)
                first_line = (left_mid + 1) * " " + (left_w - left_mid - 1) * "_" + s
                second_line = left_mid * " " + "/" + (left_w - left_mid - 1 + u) * " "
                shifted_left = [line + " " * u for line in left_lines]
                return [first_line, second_line] + shifted_left, left_w + u, left_h + 2, left_w + u // 2

            if node.left is None:
                # Only right child.
                right_lines, right_w, right_h, right_mid = _display_aux(node.right)
                s = str(node.val)
                u = len(s)
                first_line = s + right_mid * "_" + (right_w - right_mid) * " "
                second_line = (u + right_mid) * " " + "\\" + (right_w - right_mid - 1) * " "
                shifted_right = [" " * u + line for line in right_lines]
                return [first_line, second_line] + shifted_right, right_w + u, right_h + 2, u // 2

            # Two children.
            left_lines, left_w, left_h, left_mid = _display_aux(node.left)
            right_lines, right_w, right_h, right_mid = _display_aux(node.right)
            s = str(node.val)
            u = len(s)
            first_line = (left_mid + 1) * " " + (left_w - left_mid - 1) * "_" + s + right_mid * "_" + (right_w - right_mid) * " "
            second_line = left_mid * " " + "/" + (left_w - left_mid - 1 + u + right_mid) * " " + "\\" + (right_w - right_mid - 1) * " "
            if left_h < right_h:
                left_lines += [" " * left_w] * (right_h - left_h)
            elif right_h < left_h:
                right_lines += [" " * right_w] * (left_h - right_h)
            merged_lines = [l + " " * u + r for l, r in zip(left_lines, right_lines)]
            return [first_line, second_line] + merged_lines, left_w + right_w + u, max(left_h, right_h) + 2, left_w + u // 2

        if root is None:
            print("The tree is empty.")
            return
        lines, _, _, _ = _display_aux(root)
        for line in lines:
            print(line)