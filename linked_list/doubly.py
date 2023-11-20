class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if prev_node is None:
            print("Previous node should be in the linked list.")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        if prev_node.next:
            prev_node.next.prev = new_node
        prev_node.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
        new_node.prev = last_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

# Example usage:
doubly_linked_list = DoublyLinkedList()

doubly_linked_list.insert_at_end(1)
doubly_linked_list.insert_at_end(2)
doubly_linked_list.insert_at_end(3)

print("Doubly Linked List:")
doubly_linked_list.display()

doubly_linked_list.insert_at_beginning(0)
doubly_linked_list.insert_after_node(doubly_linked_list.head.next, 1.5)

print("\nDoubly Linked List after insertion:")
doubly_linked_list.display()
