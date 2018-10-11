import random #用于测试
 
 
class Heap(object):#这是个最小值堆
    def __init__(self,mylist=None):
        self.__size=0
        self.__heaplist=[]
        #两种建堆方式，一种是一个一个插，另一种是直接载入一个列表
        if type(mylist)==type(self.__heaplist):
            self.__heaplist=mylist
            self.__size = len(mylist)
            self.build_heap()
 
    def is_leaf(self,pos):#因为是完全二叉树，是否是叶子结点很容易写出
        return (pos>=self.__size//2)and(pos<self.__size)
 
    def left_child(self,pos):
        return 2*pos+1
 
    def right_child(self,pos):
        return 2*pos+2
 
    def parent(self,pos):
        return pos//2
 
    def get_size(self):
        return self.__size
 
    #这个函数的用法是把某一结点通过沉降达到适合的位置，最小值堆的话比子节点大就下沉
    def shift_down(self,pos):
        while(not self.is_leaf(pos)):
            min_child=self.left_child(pos)
            rc=self.right_child(pos)
            if (rc<self.__size)and(self.__heaplist[rc]<self.__heaplist[min_child]):
                min_child=rc
            if self.__heaplist[pos]<=self.__heaplist[min_child]:
                return
            self.__heaplist[pos],self.__heaplist[min_child]=self.__heaplist[min_child],self.__heaplist[pos]
            pos=min_child
    #这个就是shift_down的逆用法了
    def push_up(self,pos):
        while (pos !=0) and (self.__heaplist[pos]<self.__heaplist[self.parent(pos)]):
            self.__heaplist[pos],self.__heaplist[self.parent(pos)]=self.__heaplist[self.parent(pos)],self.__heaplist[pos]
            pos=self.parent(pos)
 
    def build_heap(self):
        if self.__size == 0:
            return
        child=self.__size-1
        pnt=self.parent(child)
        for i in range(pnt,-1,-1):#范围是pnt到0的循环
            self.shift_down(i)
 
    def insert(self,data):
        pos=self.__size
        self.__size+=1
        self.__heaplist.append(data)
        self.push_up(pos)
 
    def remove_first(self):
        if self.__size ==0:
            return
        self.__heaplist[self.__size-1],self.__heaplist[0]=self.__heaplist[0],self.__heaplist[self.__size-1]
        self.__size-=1
        if(self.__size !=0):
            self.shift_down(0)
        return self.__heaplist.pop()
 
    def remove_pos(self,pos):
        if self.__size ==0:
            return
        if pos==self.__size-1:
            self.__size-=1
        else:
            self.__heaplist[self.__size - 1], self.__heaplist[pos] = self.__heaplist[pos], self.__heaplist[self.__size - 1]
            self.__size-=1
            #只可能是push_up或者shift_down,又或者不动
            self.push_up(pos)
            if self.__size!=0:
                self.shift_down(pos)
        return self.__heaplist.pop()


list1=list(range(3))
random.shuffle(list1)
print(list1)
#两种建堆
h=Heap(list1)
for i in range(3):
    print(h.remove_first())
 
for i in range(3):
    h.insert(i)
print(' ')
for i in range(3):
    print(h.remove_first())
