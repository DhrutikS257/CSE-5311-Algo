import logging

logging.basicConfig(format='%(asctime)s %(message)s')

class Queue:
    def __init__(self, size: int = 12):
        self.q = [None] * size
        self.head = 0
        self.tail = 0
        self.size = size
        self.count = 0 
    
    def enqueue(self, num: int) -> None:
        if self.count == self.size:
            logging.error(f"Cannot enqueue {num}, queue is full.")
            return
        self.q[self.tail] = num
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def dequeue(self) -> int:
        if self.count == 0:
            logging.error("Cannot dequeue, queue is empty.")
            return None
        x = self.q[self.head]
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return x

    def __str__(self) -> str:
        if self.count == 0:
            return "Queue is empty."
        
        items = []
        index = self.head
        for _ in range(self.count):
            items.append(str(self.q[index]))
            index = (index + 1) % self.size
        return "Queue: " + ", ".join(items)
