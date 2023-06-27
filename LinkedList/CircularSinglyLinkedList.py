class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        value = ''
        ll = self.length
        if not self.head:
            value = 'None'
        else:
            pointer = self.head
            while ll > 0:
                value = value + str(pointer.value) + '->'
                pointer = pointer.next
                ll -= 1
        return value

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
            self.tail.next = self.head
        else:
            temp = self.tail
            self.tail = node
            temp.next = self.tail
            self.tail.next = self.head
        self.length += 1

    def insert(self, pos, value):
        node = Node(value)
        isInserted = True
        if pos < -1 or pos >= self.length or (self.head is None and pos > 0):
            isInserted = False
        elif self.head is None and pos == 0:
            self.head = value
            self.tail = value
        elif pos == -1:
            temp = self.tail
            self.tail = node
            temp.next = self.tail
            self.tail.next = self.head
            self.length += 1
        else:
            pointer = self.head
            temp = None
            for _ in range(pos):
                temp = pointer
                pointer = pointer.next
            temp.next = node
            node.next = pointer
            self.length += 1
        return isInserted

    def delete(self, pos):
        if pos >= self.length or self.head is None:
            return None
        elif pos == 0:
            temp = self.head
            self.head = self.head.next
            self.tail.next = self.head
            self.length -= 1
            return temp.value
        else:
            temp = pointer = self.head
            for _ in range(pos):
                temp = pointer
                pointer = pointer.next
            temp.next = pointer.next
            self.length -= 1
            return pointer.value

    def get_length(self):
        return self.length

    def searchList(self, val):
        isExist = False
        temp = self.head
        if not temp:
            isExist = False
        else:
            while temp:
                if temp.value == val:
                    isExist = True
                    break
                elif temp is self.tail:
                    break
                else:
                    temp = temp.next

        return isExist

    def deleteAll(self):
        self.head = None
        self.tail.next = None
        self.tail = None
        self.length = 0


csll = CircularSinglyLinkedList()

csll.append(1)
csll.append(2)
csll.append(3)
print(csll.get_length())
print(csll)
print()
print(csll.insert(1, 1.5))
print(csll)
print()
print(csll.insert(3, 2.5))
print(csll)
print()
print(csll.insert(-1, 3.5))
print(csll)
print()
print()
print(csll.delete(0))
print(csll)
print()
print(csll.delete(1))
print(csll)
print(csll.searchList(6))
print(csll.searchList(3))

