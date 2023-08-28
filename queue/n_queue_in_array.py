"""ADS_CSCSC01/queue/n_queue_in_array.py
Lab: 2 -
Implement N queues in a given Array of Size N. 
Show the values of the Front, Rear , Boundary pointers for each queue in 
graphical form after very addition and deletion operation.
"""
from typing import List, Optional


class NQueuesInArray:
    def __init__(self, no_of_queues: int, array_size: int):
        self.no_of_queues: int = no_of_queues
        self.array_size: int = array_size
        self.array: List[int] = [-1]*array_size
        self.front: List[int] = [-1]*array_size
        self.rear: List[int] = [-1]*array_size
        self.next_array: List[int] = [i+1 for i in range(array_size)]
        self.next_array[array_size-1] = -1
        self.free: int = 0

    
    def is_empty(self, queue_no: int) -> bool:
        return self.front[queue_no] == -1


    def is_full(self) -> bool:
        return self.free == -1


    def enqueue(self, item: int, queue_no: int) -> None:
        if self.is_full():
            print("Queue Overflow")
            return

        next_free = self.next_array[self.free]
        if self.is_empty(queue_no):
            self.front[queue_no] = self.rear[queue_no] = self.free
        else:
            self.next_array[self.rear[queue_no]] = self.free
            self.rear[queue_no] = self.free

        self.next_array[self.free] = -1
        self.array[self.free] = item
        self.free = next_free


    def dequeue(self, queue_no: int) -> Optional[int]:
        if self.is_empty(queue_no):
            print("Queue Underflow")
            return None

        front = self.front[queue_no]
        self.front[queue_no] = self.next_array[front]
        self.next_array[front] = self.free
        self.free = front
        return self.array[front]


    def display(self, queue_no: int) -> None:
        if self.is_empty(queue_no):
            print("Queue is empty")
            return

        front = self.front[queue_no]
        while front != -1:
            print(self.array[front], end=" ")
            front = self.next_array[front]
        print()


if __name__ == '__main__':
    n_queues = NQueuesInArray(no_of_queues=5, array_size=20)

    n_queues.enqueue(10, 0)
    n_queues.enqueue(20, 2)
    n_queues.enqueue(30, 3)
    n_queues.enqueue(40, 3)
    n_queues.enqueue(40, 4)

    n_queues.display(0)
    n_queues.display(1)
    n_queues.display(2)

    print(n_queues.dequeue(0))
    print(n_queues.dequeue(3))
    print(n_queues.dequeue(4))
