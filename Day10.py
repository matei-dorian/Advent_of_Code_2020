f = open("Input")
L = [int(n) for n in f.readlines()]   # we create a list with all the numbers
L = [0]+L
L.sort()
ct1=0
ct3=0
mjolt = L[len(L)-1]+3

L = L+[mjolt]
D = [0]*(len(L)+1)
D[0] = 3
for i in range(1,len(L)):
    if L[i]-L[i-1] == 1:
        ct1 += 1
        D[i] =1
    elif L[i]-L[i-1] == 3:
        ct3 += 1
        D[i] = 3



print(ct1*ct3)
print(len(D))
# for task 2
ct1= 0
p =1
for i in range(0,len(D)):
    if D[i] == 3:
        j = i+1
        ct1 = 0
        while j <= len(D) and D[j]==1:
            ct1 += 1
            j += 1
        if ct1 == 2:
            p=p*2
        elif ct1 == 3:
            p=p*4
        elif ct1==4:
            p=p*7


print(D)
print(p)
