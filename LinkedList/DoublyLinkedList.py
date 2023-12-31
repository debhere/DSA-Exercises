class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        value = ''
        pointer = self.head
        while pointer:
            value = value + '<- ' + str(pointer.value) + ' ->'
            pointer = pointer.next
        return value

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            temp = self.tail
            self.tail = node
            temp.next = self.tail
            self.tail.prev = temp
        self.length += 1

    def insertNode(self, index, value):
        node = Node(value)
        isInserted = False
        if index > self.length or index < -1:
            isInserted = False
        elif self.head is None and index == 0:
            self.head = node
            self.tail = node
            self.length += 1
            isInserted = True
        elif index == 0:
            pointer = self.head
            self.head = node
            self.head.next = pointer
            pointer.prev = self.head
            self.length += 1
            isInserted = True
        elif index == self.length or index == -1:
            pointer = self.tail
            self.tail = node
            self.tail.prev = pointer
            pointer.next = self.tail
            self.length += 1
            isInserted = True
        else:
            pointer, temp = self.head, None
            for _ in range(index):
                temp = pointer
                pointer = pointer.next

            temp.next = node
            node.prev = temp
            node.next = pointer
            pointer.prev = node
            self.length += 1
            isInserted = True

        return isInserted

    def deleteNode(self, index):
        delVal = None
        if not self.head or index >= self.length:
            delVal = None
        elif self.length == 1 and index == 0:
            delVal = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            pointer = self.head
            for _ in range(index):
                pointer = pointer.next
            delVal = pointer.value
            temp = pointer.prev
            temp.next = pointer.next
            pointer.next.prev = temp
            self.length -= 1
        return delVal

    def get_length(self):
        return self.length


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
print(dll)
print()
dll.insertNode(0, 0)
dll.insertNode(2, 1.5)
dll.insertNode(6, 5)
dll.insertNode(-1, 6)
print(dll)
print()
dll.deleteNode(1)
print(dll)
print(dll.get_length())

for node in dll:
    print(node.value)


