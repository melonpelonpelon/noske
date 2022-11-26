S = list(input())
S = [int(i) for i in S]
a = [i for i,x in enumerate(S) if x == 0]
b = [[]for _ in range(7)]
b[0].append(S[9])
b[1].append(S[5])
b[2].append(S[8])
b[2].append(S[2])
b[3].append(S[4])
b[3].append(S[0])
b[4].append(S[7])
b[4].append(S[1])
b[5].append(S[3])
b[6].append(S[6])
flag = False
flag_2= False
if S[0] == 0:
    for i in range(1,7):
        if b[i].count(1) == 0:
            for j in range(i):
                if b[j].count(0) == 0:
                    flag = True
            for k in range(i,7):
                if b[k].count(0) == 0:
                    flag_2 = True
    if flag and flag_2:
        print("Yes")
    else:
        print("No")
else:
    print("No")