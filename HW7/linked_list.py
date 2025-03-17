import logging
from typing import Optional
logging.basicConfig(format='%(asctime)s %(message)s')

class Node:

    def __init__(self, val: Optional[int], next: Optional['Node'] = None):

        self.val = val

        self.next = next

class LinkedList:

    def __init__(self):

        self.head:Node = None

    def insert(self, n: Node):

        if self.head is None:
            self.head = n

        else:
            lastNode = self.head

            while lastNode.next:
                lastNode = lastNode.next

            lastNode.next = n


    def delete(self, del_val:int):

        prev_node, search_node = self._del_search(del_val)

        if search_node is None:
            return

        if prev_node is None:

            self.head = search_node.next

        else:
            prev_node.next = search_node.next

        search_node.next = None
    
    def _del_search(self, val: int) -> tuple[Optional[Node], Optional[Node]]:

        prev_node = None
        search_node = self.head

        while search_node:
            if search_node.val == val:
                return (prev_node, search_node)

            prev_node = search_node
            search_node = search_node.next

        logging.error(f"List doesn't contain any node with value: {val}")
        return (None, None)


    def search(self, val:int) -> Optional[Node]:

        current = self.head

        while current:

            if current.val == val:
                return current
            
            current = current.next

        logging.error(f"List doesn't contain any node with value: {val}")
        return None


