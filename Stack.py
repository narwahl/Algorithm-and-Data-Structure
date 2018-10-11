class Node():
    def __init__(self,value):
        self.value = value
        self.point = None

class Stack():
    def __init__(self):
        self.lian = None

    def IsEmpty(self):
        if self.lian is None:
            print("Empty Stack")
        print("Not Empty Stack")

    def size(self):
        size = self.lian
        count = 0
        if size is None:
            print("Empty Stack")
        while size != None:
            count += 1
            size = size.next
        return count

    def push(self,value):
        jiedian = Node(value)
        jiedian.next = self.lian
        self.lian = jiedian

    def pop(self):
        paochu = self.lian
        if self.lian is None:
            print("Empty Satck")
        self.lian = paochu.next
        return paochu.value

if __name__ == '__main__':
    s= Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())