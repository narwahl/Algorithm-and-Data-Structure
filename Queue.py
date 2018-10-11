class Node():
    def __init__(self,value):
        self.point = None
        self.value = value

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.__count = 0

    def isEmpty(self):
        return  self.first == None 

    def size(self):
        return self.__count
         
    def enqueue(self,value):
        into = Node(value)
        if self.isEmpty():
            self.first = into
        else:
            self.last.point = into
          
        self.last = into
        self.__count += 1


    def dequeue(self):
        if self.isEmpty():
            return False
        out = self.first
        if self.first == self.last:
            return out.value
        else:
            self.first = self.first.point
            self.__count -= 1
            return out.value
    

        
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())