import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    
    def setUp(self):
        self.stack = Stack(size=5)
    
    def test_empty_stack(self):

        self.assertTrue(self.stack.stack_empty(), "Stack should be empty upon initialization.")
        self.stack.push(10)
        self.assertFalse(self.stack.stack_empty(), "Stack should not be empty after a push.")
    
    def test_push_and_top(self):

        self.stack.push(5)
        self.assertEqual(self.stack.top(), 5, "Top element should be 5 after push.")
        self.stack.push(15)
        self.assertEqual(self.stack.top(), 15, "Top element should be 15 after second push.")
    
    def test_pop(self):

        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.pop()
        self.assertEqual(self.stack.top(), 2, "After one pop, top should be 2.")
        self.stack.pop()
        self.assertEqual(self.stack.top(), 1, "After second pop, top should be 1.")
        self.stack.pop()
        self.assertTrue(self.stack.stack_empty(), "Stack should be empty after popping all elements.")
    
    def test_overflow(self):

        for i in range(5):
            self.stack.push(i)

        with self.assertLogs(level='ERROR') as cm:
            self.stack.push(99)
        self.assertIn("Cannot push 99, max length of array reached.", cm.output[0])

        self.assertEqual(self.stack.top(), 4, "Top should remain 4 after failed push.")
    
    def test_pop_empty(self):

        with self.assertLogs(level='ERROR') as cm:
            self.stack.pop()
        self.assertIn("Cannot pop, stack is empty.", cm.output[0])

    def test_push_print(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        print(self.stack)
        self.assertEqual(str(self.stack), "Stack: 10, 20, 30")

    def test_pop_print(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.pop()
        print(self.stack)
        self.assertEqual(str(self.stack), "Stack: 1, 2")


if __name__ == "__main__":
    unittest.main()
