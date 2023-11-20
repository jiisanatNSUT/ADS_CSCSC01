class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node  # Point to itself for circularity
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node should be in the linked list.")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            new_node.next = new_node  # Point to itself for circularity
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("Empty Circular Linked List")
            return

        current_node = self.head
        while True:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
            if current_node == self.head:
                break
        print("(head)")

# Example usage:
circular_linked_list = CircularLinkedList()

circular_linked_list.insert_at_end(1)
circular_linked_list.insert_at_end(2)
circular_linked_list.insert_at_end(3)

print("Circular Linked List:")
circular_linked_list.display()

circular_linked_list.insert_at_beginning(0)
circular_linked_list.insert_after_node(circular_linked_list.head.next, 1.5)

print("\nCircular Linked List after insertion:")
circular_linked_list.display()
