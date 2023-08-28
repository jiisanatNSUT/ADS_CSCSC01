"""ADS_CSCSC01/queue/stack_with_queue.py
Lab: 2 -
2.3. Implement the Stack using two Queues
"""

from _collections import deque

class StackWithQueue:

    def __init__(self) -> None:
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, value: int) -> None:
        self.queue1.append(value)

    def pop(self) -> int:
        if not self.queue1:
            raise IndexError("Stack is empty")
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return self.queue2.popleft()

    def top(self) -> int:
        if not self.queue1:
            raise IndexError("Stack is empty")

        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.popleft())

        top = self.queue1[0]
        self.queue2.append(self.queue1.popleft())

        self.queue1, self.queue2 = self.queue2, self.queue1
        return top

    def size(self) -> int:
        return len(self.queue1)


if __name__ == '__main__':
    s = StackWithQueue()
    s.push(1)
    s.push(2)
    s.push(3)

    print("current size: ", s.size())
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())

    print("current size: ", s.size())
