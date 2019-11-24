class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class CircleList:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head == None:
            self.head = Node(value)
            self.head.next = self.head
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

    def action(self):
        current = self.head
        temp = current.value
        while current.next != self.head:
            current.next.value, temp = current.next.value - temp, current.next.value
            current = current.next
        current.next.value -= temp

        s = ""
        current = self.head
        while current.next != self.head:
            s += str(current.value) + ", "
            current = current.next
        s += str(current.value)
        return s