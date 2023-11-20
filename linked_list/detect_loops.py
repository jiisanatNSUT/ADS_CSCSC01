class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_loop(head):
    tortoise = head
    hare = head

    while hare is not None and hare.next is not None:
        tortoise = tortoise.next
        hare = hare.next.next

        if tortoise == hare:
            return True  # Loop detected

    return False  # No loop detected

# Example usage:
# Create a linked list with a loop
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2  # Creating a loop

loop_detected = detect_loop(head)

if loop_detected:
    print("Loop detected in the linked list.")
else:
    print("No loop detected in the linked list.")
