class Select():
    def __init__(self,value = []):
        self.value = value

    def select_list(self):
        r = self.value
        for i in range(0, len(r)-1):
            for j in range(i + 1, len(r)):
                if r[i] > r[j]:
                    temp = r[i]
                    r[i] = r[j]
                    r[j] = temp
        return r

pai = Select([6,3,2,7,8,9,0,1])
print(pai.select_list()) 