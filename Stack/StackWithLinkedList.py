class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackWithLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

    def __str__(self):
        values = [str(x.value) for x in self.__iter__()]
        return '\n'.join(values)

    def isEmpty(self):
        isVoid = True
        if self.head:
            isVoid = False
        return isVoid

    def push(self, element):
        message = 'None'
        node = Node(element)
        if self.length == 0:
            self.head = node
            self.length += 1
            message = '{} is added'.format(node.value)
        else:
            temp = self.head
            self.head = node
            self.head.next = temp
            self.length += 1
            message = '{} is added'.format(node.value)
        return message

    def pop(self):
        poppedNode = None
        if self.length > 0:
            temp = self.head
            self.head = temp.next
            poppedNode = temp
            self.length -= 1
        return poppedNode.value


stackLinkedList = StackWithLinkedList()
print(stackLinkedList.isEmpty())
print(stackLinkedList.push(3))
print(stackLinkedList.push(2))
print(stackLinkedList.push(1))
print(stackLinkedList.push(0))
print(stackLinkedList.push(-1))
print(stackLinkedList.isEmpty())
print(stackLinkedList)
print(stackLinkedList.pop())
print(stackLinkedList)
print(stackLinkedList.head.value)
