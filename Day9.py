f = open("Input")
L = [int(n) for n in f.readlines()]   # we create a list with all the numbers


for i in range(25,len(L)):
    S = set(L[i-25:i])  # we create a set with the range of numbers that we can add up
    ok = 0              # if ok stays 0 then we found the bad number
    for n in S:
        m = L[i]-n
        if m!=n and m in S:
            ok = 1
            break
    if ok==0:
        print(L[i])
        break
    #print(S)

N = L[i]
L[i] =0

Sum = [0]*(i+1)
Sum[0] = L[0]
for j in range(1,i):
    Sum[j] += Sum[j-1] + L[j]

for p in range(0,i):
    for q in range(p+1,i):
        r = Sum[q] - Sum[p]+L[p]

        if r == N:
            print(max(*L[p:q+1])+min(*L[p:q+1]))
            break

# print(Sum)
# print(L)
exit()
