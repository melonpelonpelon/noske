N = int(input())
array = [list(map(int,input().split())) for i in range(N)]
flag = True
if array[0][0]-array[0][1]-array[0][2] < 0 or array[0][0]%2 != (array[0][1]+array[0][2])%2:
    print("No")
    flag = False
if flag:
    for i in range(1,N):
        t = array[i-1][0]
        x = array[i-1][1]
        y = array[i-1][2]
        ti = array[i][0]
        xi = array[i][1]
        yi = array[i][2]
        if ti-t-(abs(xi-x)+abs(yi-y)) < 0 or (ti-t)%2 != ((abs(xi-x)+abs(yi-y)))%2:
            print("No")
            break
    else:
        print("Yes")