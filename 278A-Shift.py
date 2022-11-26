N,K = map(int,input().split())
array = list(input().split())
for i in range(K):
    array.pop(0)
    array.append("0")
print(" ".join(array))
