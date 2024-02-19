from node import Node


class CircularList:
    def __init__(self):
        self.head = None
        self.is_running = False

    def is_empty(self):
        return self.head is None

    def print_list(self):
        if self.is_empty():
            print("La lista esta vacia")
            return

        current = self.head
        while True:
            print(current.data, end="->")
            current = current.next
            if current == self.head:
                break
        print()

    def add_element(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete_element(self, data):
        if self.is_empty():
            print('La lista esta vacia')
            return

        if self.head.data == data:
            current = self.head
            while current.next != self.head:
                current = current.next
            if self.head == self.head.next:
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
        else:
            current = self.head
            prev = None
            while True:
                if current.data == data:
                    prev.next = current.next
                    break
                prev = current
                current = current.next
                if current == self.head:
                    break

    def edit_element(self, search_data, new_data):
        if self.is_empty():
            print("La lista esta vacia")
            return
        current = self.head
        while True:
            if current.data == search_data:
                current.data = new_data
                return
            current = current.next
            if current == self.head:
                print(f"El elemento {search_data} no esta en la lista")
                return

    def rotate(self):
        if not self.is_empty() and self.is_running:
            self.head = self.head.next

    def stop(self):
        self.is_running = True

    def star(self):
        self.is_running = False

    def next_seat(self):
        if self.is_running:
            self.rotate()

    def prev_seat(self):
        if self.is_running:
            current = self.head
            while current.next != self.head:
                prev = current
                current = current.next
            self.head = prev

    def show_seat(self):
        if not self.is_empty():
            print(f"Asiento actual: {self.head.data}")
        else:
            print("La lista está vacía")

    def clear_circular_list(self):
        self.head = None