N,M = map(int,input().split())
num = list(map(int,input().split()))
max = 0
for i in range(N-M+1):
    sum = 0
    s = num[i:M+i]
    for j in range(M):
        sum += s[j]*(j+1)
    if sum > max:
        max = sum
print(max)