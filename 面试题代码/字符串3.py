s = "hello world"
l = list(s)
for i in range(0, len(l)):
    for j in range(i + 1, len(l)):
        first = l[i]
        second = l[j]
        if first > second:
            l[i] = l[j]
            l[j] = first
s = "".join(l)
print(s)



