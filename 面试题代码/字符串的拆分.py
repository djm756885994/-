import re
s = "aAsnr3id2d4b6gs7DZsf9e1AF"
l1 = re.findall("[\d]", s)
l2 = re.findall("[\D]", s)
str = "".join(l2)
str1 = str.lower()
l3 = list(str1)
for i in range(0, len(l1)):
    for j in range(i + 1, len(l1)):
        first = l1[i]
        second = l1[j]
        if first > second:
            l1[i] = l1[j]
            l1[j] = first
s1 = "".join(l1)
for i in range(0, len(l2)):
    for j in range(i + 1, len(l3)):
        first = l3[i]
        second = l3[j]
        if first > second:
            l3[i] = l3[j]
            l3[j] = first
s2 = "".join(l3)
print(s1)
print(s2)

