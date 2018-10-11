class Insertion():
    def __init__(self,value = []):
        self.value = value

    def Insertion_list(self):
        r = self.value
        for i in range(1, len(r)):
            j = 0
            while j < i:
                if r[j] > r[i]:
                    temp = r[i]
                    r[i] = r[j]
                    r[j] = temp
                j += 1
        return r


s = Insertion([2,3,7,1,3,5,9])
print(s.Insertion_list())