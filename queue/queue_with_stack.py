"""ADS_CSCSC01/queue/queue_with_stack.py
Lab: 2 -
2.2. Implement the Queue using only functions of stack
"""

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # For enqueue operation
        self.stack2 = []  # For dequeue operation

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                raise IndexError("Queue is empty")
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

# Example usage
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
