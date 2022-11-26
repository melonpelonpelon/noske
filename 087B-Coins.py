A = int(input())
B = int(input())
C = int(input())
X = int(input())
remain = X
counter = 0
for i in range(0,C+1):
    c = remain-50*i
    if c < 0:
        break
    elif c == 0:
        counter += 1
        break
    else:
        for j in range(0,B+1):
            b = c-100*j
            if b < 0:
                break
            elif b == 0:
                counter += 1
                break
            else:
                for k in range(A):
                    a = b-500*(k+1)
                    if a < 0:
                        break
                    elif a == 0:
                        counter += 1
                        break

print(counter)

#解答例
'''
a = int(input())
b = int(input())
c = int(input())
x = int(input())

counter = 0

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if 500 * i + 100 * j + 50 * k == x:
                counter += 1

print(counter)
'''