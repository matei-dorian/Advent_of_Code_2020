f = open("Input")
L = [code for code in f.readlines()]
LID = [] # set of the IDs
ID = -1
for code in L:
    lg = 128  # total length = left + right + 1
    left = 0
    right = 127

    for i in range(7):
        lg = (left + right + 1) // 2
        if code[i] == 'F':
            right = lg - 1
        elif code[i] == 'B':
            left = lg + 1
    row = min(left, right)

    left = 0
    right = 7

    for i in range(7, 10):
        lg = (left + right + 1) // 2
        if code[i] == 'L':
            right = lg - 1
        elif code[i] == 'R':
            left = lg + 1
    col = min(left, right)
    LID.append(row*8+col)
    ID = max(ID,row * 8 + col)
print(ID)

LID.sort()
#print(LID)
n = len(LID)
for i in range(n-1):
    if LID[i+1]-LID[i] == 2:
        print(LID[i]+1)
        exit()
