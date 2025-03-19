import unittest
from linked_list import LinkedList, Node

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_insert(self):
        self.linked_list.insert(Node(10))
        self.linked_list.insert(Node(20))
        self.linked_list.insert(Node(30))
        
        self.assertEqual(self.linked_list.head.val, 10, "Head value should be 10")
        self.assertEqual(self.linked_list.head.next.val, 20, "Second node value should be 20")
        self.assertEqual(self.linked_list.head.next.next.val, 30, "Third node value should be 30")

    def test_search(self):
        self.linked_list.insert(Node(1))
        self.linked_list.insert(Node(2))
        self.linked_list.insert(Node(3))
        
        self.assertEqual(self.linked_list.search(2).val, 2, "Search should return node with value 2")
        self.assertIsNone(self.linked_list.search(99), "Search should return None for missing values")

    def test_delete(self):
        self.linked_list.insert(Node(5))
        self.linked_list.insert(Node(10))
        self.linked_list.insert(Node(15))
        
        self.linked_list.delete(10)
        
        self.assertIsNone(self.linked_list.search(10), "Deleted node should not be found")
        self.assertEqual(self.linked_list.head.val, 5, "Head should remain unchanged")
        self.assertEqual(self.linked_list.head.next.val, 15, "Remaining node should be 15")

    def test_delete_head(self):
        self.linked_list.insert(Node(100))
        self.linked_list.insert(Node(200))
        
        self.linked_list.delete(100)
        
        self.assertEqual(self.linked_list.head.val, 200, "Head should now be 200 after deleting 100")

    def test_delete_nonexistent(self):
        self.linked_list.insert(Node(1))
        self.linked_list.insert(Node(2))
        
        self.linked_list.delete(99)  # Should not affect the list
        
        self.assertEqual(self.linked_list.head.val, 1, "Head should remain 1 after attempting to delete a non-existent value")
        self.assertEqual(self.linked_list.head.next.val, 2, "Second node should remain 2")

if __name__ == "__main__":
    unittest.main()
