class Quick():
    def __init__(self, value = []):
        self.value = list(value)
       
    def quickSort(self, L, low, high):
        i = low 
        j = high
        if i >= j:
            return L
        key = L[i]
        while i < j:
            while i < j and L[j] >= key:
                j = j-1                                                             
            L[i] = L[j]
            while i < j and L[i] <= key:    
                i = i+1 
            L[j] = L[i]
        L[i] = key 
        self.quickSort(L, low, i-1)
        self.quickSort(L, j+1, high)
        return L


l = [8,3,0,2,7,1,2,3]
s = Quick(l)
print(s)   
