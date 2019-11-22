class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class CircleList:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head == None:
            self.head = Node(value, self.head)
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = Node(value, self.head)

    '''def pop(self):
        if self.head.next == self.head:
            temp = self.head
            self.head = None
            return temp
        else:
            current = self.head'''

    def Head(self):
        return self.head