N = int(input())
array = list(map(int,input().split()))
array.sort(reverse=True)
Asum = 0
Bsum = 0

for i in range(N):
    if i%2==0:
        Asum += array[i]
    else:
        Bsum += array[i]
print(Asum-Bsum)