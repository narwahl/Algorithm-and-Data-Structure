class Merge():
    def sort(self,left,right):
        aux = []
        self.l = left 
        self.r = right
        a = b = 0
        while a < len(self.l) and b < len(self.r):
            if self.l[a] < self.r[b]:
                aux.append(self.l[a])
                a += 1
            else:
                aux.append(self.r[b])
                b += 1

        if a == len(self.l):
            for i in self.r[b:]:
                aux.append(i)
        else:
            for i in self.l[a:]:
                aux.append(i)

        return aux

    def Merge_sort(self,list):
        if len(list) <= 1:
            return list
        mid = len(list)//2
        left = self.Merge_sort(list[:mid])
        right = self.Merge_sort(list[mid:])
        return self.sort(left,right)

print(Merge().Merge_sort([3,6,8,2,4,0,1,3]))