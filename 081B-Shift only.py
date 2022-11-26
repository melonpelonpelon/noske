N = int(input())
s = list(map(int,input().split()))

sum = 0
flag = 0
while True:
    for i in range(N):
        if s[i]%2 != 0:
            flag = 1
    if flag == 1:
        break    
    for i in range(N):
        s[i] = s[i]/2
    sum += 1
       
print(sum)


