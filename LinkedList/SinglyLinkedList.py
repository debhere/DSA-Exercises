class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp_node = self.tail
            self.tail = new_node
            temp_node.next = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            self.head = new_node
            new_node.next = temp_node
        self.length += 1

    def insert(self, pos, value):
        if pos > self.length:
            return False
        elif self.length == 0:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        elif pos == 0 and self.length > 0:
            new_node = Node(value)
            temp_node = self.head
            self.head = new_node
            self.head.next = temp_node
            self.length += 1
            return True
        elif pos == self.length:
            new_node = Node(value)
            temp_node = self.tail
            temp_node.next = new_node
            self.tail = new_node
            self.length += 1
            return True
        else:
            new_node = Node(value)
            idx = 0
            pointer = self.head
            while idx < pos:
                temp = pointer
                pointer = pointer.next
                idx += 1
            temp.next = new_node
            new_node.next = pointer
            return True

    def __str__(self):
        val = ''
        pointer = self.head
        while pointer is not None:
            val = val + str(pointer.value) + '->'
            pointer = pointer.next

        return val


singlyLinkedList = SinglyLinkedList()

singlyLinkedList.insert(0, 40)
singlyLinkedList.insert(1, 10)
singlyLinkedList.insert(2, 5)
singlyLinkedList.insert(0, 20)
singlyLinkedList.append(50)
singlyLinkedList.prepend(70)

print(singlyLinkedList)
