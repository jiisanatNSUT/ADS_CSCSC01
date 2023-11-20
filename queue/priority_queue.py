"""ADS_CSCSC01/queue/priority_queue.py
Lab: 2 -
2.4.  Implement the priority Queues using the 2 Dimensional Array. 
Show all the add and delete operation in graphical form. in python
"""
from typing import List


class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []
        
    def add(self, element: int, priority: int) -> None:
        self.queue.append([element, priority])
        
    def delete(self) -> None:
        if self.queue:
            highest_priority_index = 0
            highest_priority = self.queue[0][1]
            
            for i in range(1, len(self.queue)):
                if self.queue[i][1] < highest_priority:
                    highest_priority = self.queue[i][1]
                    highest_priority_index = i
                    
            del self.queue[highest_priority_index]
            
    def display(self) -> List[int]:
        for item in self.queue:
            print(item)


if __name__ == '__main__':
    pq = PriorityQueue()

    pq.add("Task 1", 3)
    pq.add("Task 2", 1)
    pq.add("Task 3", 2)
    pq.add("Task 4", 5)

    print("Initial Queue:")
    pq.display()

    pq.delete()

    print("\nQueue after delete operation:")
    pq.display()
