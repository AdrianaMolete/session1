def split_pairs(a):
    solutie = []

    if len(a) % 2 != 0:
        a += "_"

    for i in range(0, len(a), 2):
        solutie.append(a[i : i + 2])
    return solutie
print(split_pairs("abc"))
print (split_pairs("abcdef"))






a = "This is an example!"
words = a.split()
invers = ""
for word in words:
    for c in reversed(word):
        invers += c
    invers += " "
print(invers)






class Human:
    def __init__ (self, name):
        self.name = name

class Adam(Human):
    pass
class Eva(Human):
    pass
def rezolvare():
    return[Adam('a'), Eva('e')]

x, y = rezolvare()
print(type(x))
print(type(y))
print(isinstance(x,Adam))
print(isinstance(x,Human))