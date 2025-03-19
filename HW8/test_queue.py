import unittest
from queue import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):

        self.queue = Queue(size=5)

    def test_enqueue_dequeue(self):

        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        
        self.assertEqual(self.queue.dequeue(), 10, "First dequeued element should be 10")
        self.assertEqual(self.queue.dequeue(), 20, "Second dequeued element should be 20")
        self.assertEqual(self.queue.dequeue(), 30, "Third dequeued element should be 30")

        self.assertIsNone(self.queue.dequeue(), "Dequeueing an empty queue should return None")

    def test_wrap_around(self):

        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        
        self.queue.enqueue(6)
        self.queue.enqueue(7)
        

        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.dequeue(), 4)
        self.assertEqual(self.queue.dequeue(), 5)
        self.assertEqual(self.queue.dequeue(), 6)
        self.assertEqual(self.queue.dequeue(), 7)

    def test_str_representation(self):

        self.assertEqual(str(self.queue), "Queue is empty.", "Empty queue string representation incorrect")
        self.queue.enqueue(100)
        self.queue.enqueue(200)
        self.queue.enqueue(300)
        expected_str = "Queue: 100, 200, 300"
        self.assertEqual(str(self.queue), expected_str, "Queue string representation incorrect")
        print(str(self.queue))

if __name__ == "__main__":
    unittest.main()
