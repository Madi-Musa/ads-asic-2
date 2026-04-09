class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_the_beginning(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end="->")
            current = current.next

ll = LinkedList()

ll.add_the_beginning(5)
ll.add_the_beginning(10)
ll.add_the_beginning(20)
ll.print_list()


class Node:
    def __init__(self, num):
        self.num =  num
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_the_end(self, num):
        new_node =  Node(num)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.num, end="->")
            temp = temp.next

ll = LinkedList()
ll.add_the_end(5)
ll.add_the_end(10)
ll.add_the_end(20)

ll.print_list()


class Node:
    def __init__(self, num):
        self.num = num
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_the_last(self, num):
        new_node = Node(num)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def remove_the_last(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.num)
            temp = temp.next

ll = LinkedList()

ll.add_the_last(5)
ll.add_the_last(10)
ll.add_the_last(15)
ll.add_the_last(20)
ll.add_the_last(25)

ll.remove_the_last()
ll.print_list()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_num(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next

ll = LinkedList()
ll.add_to_num(10)
ll.add_to_num(20)
ll.add_to_num(30)
ll.print_list()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_number(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def search(self, data):
        temp = self.head

        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

ll = LinkedList()
ll.add_number(10)
ll.add_number(20)
ll.add_number(30)
print(ll.search(20))



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_number(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        count = 0

        while temp is not None and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Error position")
            return

        new_node.next = temp.next
        temp.next = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


ll = LinkedList()
ll.add_number(10)
ll.add_number(20)
ll.add_number(30)

ll.insert_at_position(40, 2)
ll.printList()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_number(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_by_value(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next is not None and temp.next.data != value:
            temp = temp.next

        if temp.next is not None:
            temp.next = temp.next.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


ll = LinkedList()
ll.add_number(10)
ll.add_number(20)
ll.add_number(30)

ll.remove_by_value(20)
ll.printList()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_number(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def combine(self, other):
        if self.head is None:
            self.head = other.head
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = other.head

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


ll1 = LinkedList()
ll1.add_number(10)
ll1.add_number(20)

ll2 = LinkedList()
ll2.add_number(5)
ll2.add_number(15)

ll1.combine(ll2)
ll1.printList()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_number(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


ll = LinkedList()
ll.add_number(10)
ll.add_number(20)
ll.add_number(30)

ll.reverse()
ll.printList()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_number(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def sort_list(self):
        current = self.head

        while current:
            index = current.next
            while index:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


ll = LinkedList()
ll.add_number(10)
ll.add_number(30)
ll.add_number(20)

ll.sort_list()
ll.printList()