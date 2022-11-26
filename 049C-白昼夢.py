str = input()
a = str.count("dream")
b = str.count("dreamer")
c = str.count("erase")
d = str.count("eraser")
e = str.count("dreamerase")
sum = (a-b)*5+b*7+(c-d)*5+d*6-2*e

if sum == len(str):
    print("YES")
else:
    print("NO")