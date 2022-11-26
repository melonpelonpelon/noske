N = int(input())
array = []
counter = 1

for i in range(N):
    array.append(int(input()))
    if i == 0:
        continue
    
    for j in range(i):
        if array[j] == array[i]:
            break
    else:
        counter += 1
print(counter)