import logging

logging.basicConfig(format='%(asctime)s %(message)s')

class Stack:

    def __init__(self, size:int = 12):
        self.stack = [None] * size
        self._top = -1
    
    def stack_empty(self) -> bool:

        return True if self._top == -1 else False
    
    def push(self, num:int) -> None:
        if self._top + 1 >= len(self.stack):
            logging.error(f"Cannot push {num}, max length of array reached.")
            return
        
        self._top += 1
        self.stack[self._top] = num

    def pop(self):
        if self._top < 0:
            logging.error(f"Cannot pop, stack is empty.")
            return

        self.stack[self._top] = None
        self._top -= 1

    def top(self) -> int:
        return self.stack[self._top]
    
    def __str__(self) -> str:

        if self.stack_empty():
            return "Stack is empty."

        return "Stack: " + ", ".join(str(self.stack[i]) for i in range(self._top + 1))
