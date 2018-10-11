class Shall():
    def __init__(self, value = []):
        self.value = value

    def shell_sort(self):
        s = self.value
        step = int(len(s)/2)
        while step > 1:
            for i in range(step, len(s)):
                while  i >= step and s[i - step] > s[step]:
                    s[i], s[step] = s[step], s[i]
                    i -= step
            step = step/2
        return s

l = Shall([6,3,0,2,5,6,2,1])
print(l.shell_sort())
