N,M = map(int,input().split())
partipants = []
for i in range(M):
    array = list(map(int,input().split()))
    partipants.append(array)

check = [[0 for n in range(N)]for _ in range(N)]
for i in range(N):
    check[i][i] = 1
for i in partipants:
    for j in range(1,i[0]):
        for k in range(1,i[0]-j+1):
            check[i[j]-1][i[j+k]-1] = 1
            check[i[j+k]-1][i[j]-1] = 1
for ch in check:
    if 0 in ch:
        print("No")
        break
else:
    print("Yes")
