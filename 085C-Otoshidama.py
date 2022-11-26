array = list(map(int,input().split()))
N = array[0]
s = [-1,-1,-1]

for i in range(N+1):
    sum = array[1]
    if sum-1000*i < 0:
        continue
    elif sum-1000*i == 0:
        s = [0,0,i]
    else:
        sum -= 1000*i

        for j in range(N-i+1):
            if sum-5000*j < 0:
                continue
            elif sum-5000*j == 0:
                s = [0,j,i]
            else:
                sum -= 5000*j

                for k in range(N-i-j+1):
                    if sum-10000*k < 0:
                        break
                    elif sum-10000*k == 0:
                        s = [k,j,i]
                        break
                    
if s == [-1,-1,-1]:
    print(-1,-1,-1)
else:
    print(s[0],s[1],s[2])

        