N = int(input())
integer = list(map(int,input().split()))
evens = []
odds = []
for i in integer:
    if i%2 == 0:
        evens.append(i)
    else:
        odds.append(i)
maxs = []

if len(evens) < 2 and len(odds) < 2:
    print(-1)  

if len(evens) >= 2:
    maxs.append(max(evens))
    evens.remove(max(evens))
    maxs.append(max(evens))
    sum1 = maxs[0] + maxs[1]
    if len(odds) < 2:
        print(sum1)

if len(odds) >= 2:
    maxs.append(max(odds))
    odds.remove(max(odds))
    maxs.append(max(odds))
    sum2 = maxs[2] + maxs[3]
    if len(evens) < 2:
        print(sum2)

if len(evens) >=2 and len(odds) >=2:   
    if sum1 > sum2:
        print(sum1)
    else:
        print(sum2)