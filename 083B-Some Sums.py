array = list(map(int,input().split()))
N = array[0]
sum = 0

for i in range(N+1):
    num = i
    psum = 0

    for j in range(0,5):
       jplace = num%10
       psum += jplace
       num -= jplace
       num /= 10

       if num <= 0:
        break

    if array[1] <= psum and psum <= array[2]:
        sum += i

print(sum)

