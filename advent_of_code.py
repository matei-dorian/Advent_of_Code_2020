def Run(L):
    s = 0
    p = 0  # p points to the instruction that is about to be executed
    ok = 0 # if ok is 0 the commands for a loop if it s 1 then we terminated the execution
    n = len(L)
    for x in L:
        x[2] =0
    while L[p][2] == 0:  # as long as we haven t executed the same instruction teice
        # print(p)
        if L[p][0] == 'nop':
            L[p][2] = 1
            p += 1
        elif L[p][0] == 'acc':
            s += L[p][1]
            L[p][2] = 1
            p += 1
        else:
            L[p][2] = 1
            p += L[p][1]
        if p>=n:
            ok = 1
            break
    return p,s,ok


f = open("Input")
L = [[x[:x.find(" ")], int(x[x.find(" ")+1:]), 0] for x in f.readlines()]  # in this list the first element of each container holds the type of the instruction,
# the second element holds the argument and the last value indicats how many times we executed it
#print(L)


# task 1
p,s,ok=Run(L)
#print(p)
print(s)

for cmd in L:
    if cmd[0] == 'nop':
        cmd[0] = 'jmp'

        p, s, ok = Run(L)
        cmd[0] = 'nop'

    elif cmd[0] =='jmp':
        cmd[0] ='nop'

        p, s, ok = Run(L)
        cmd[0] = 'jmp'


    if ok == 1:
        print(s)
        exit()


print(L)