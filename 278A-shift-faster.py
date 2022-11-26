from collections import deque
N,K = map(int,input().split())
array = deque(list(input().split()))
for i in range(K):
    array.pop()
    array.append("0")
print(" ".join(array))