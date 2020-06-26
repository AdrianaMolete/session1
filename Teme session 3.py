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
b = "double spaces"
words = a.split()
invers = ""
for word in words:
    for c in reversed(word):
        invers += c
    invers += " "
print(invers)






