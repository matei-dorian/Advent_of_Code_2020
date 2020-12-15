f = open("Input")
L = [[instr[0],int(instr[1:].strip('\n'))] for instr in f.readlines()]

# task 1
# x = 0
# y = 0
# face = 1  # 1 is east, 2 is south, 3 is west, 4 is north
# print(L)
# for i in L:
#     if i[0] == 'N':
#         y = y + i[1]
#         print(x, y)
#     if i[0] == 'S':
#         y = y - i[1]
#         print(x, y)
#     if i[0] == 'E':
#         x = x + i[1]
#         print(x, y)
#     if i[0] == 'W':
#         x = x - i[1]
#         print(x, y)
#     if i[0] == 'F':
#         if face == 1:
#             x = x + i[1]
#         elif face == 2:
#             y = y - i[1]
#         elif face == 3:
#             x = x - i[1]
#         elif face == 4:
#             y = y + i[1]
#         print(x,y)
#     if i[0] == 'R':
#         d = i[1] // 90
#         face = (face+d)%4
#         if face==0:
#             face=4
#         print(face)
#     if i[0] == 'L':
#         d = i[1] // 90
#         face = (face-d)%4
#         if face==0:
#             face=4
#         print(face)
#
# print(abs(x)+abs(y))

# task 1
wx = 10 # the wayppoint
wy = 1
face = 1  # 1 is east, 2 is south, 3 is west, 4 is north
x = 0
y = 0
print(L)
for i in L:
    if i[0] == 'N':
        wy = wy + i[1]
        print(wx, wy)
    if i[0] == 'S':
        wy = wy - i[1]
        print(wx, wy)
    if i[0] == 'E':
        wx = wx + i[1]
        print(wx, wy)
    if i[0] == 'W':
        wx = wx - i[1]
        print(wx, wy)
    if i[0] == 'F':
       x = x + wx*i[1]
       y = y + wy*i[1]
    if i[0] == 'R':
       if i[1]==90:
           wx,wy=wy,wx
           wy = wy *-1
       if i[1]==180:
           wx = wx*-1
           wy = wy*-1
       if i[1]==270:
           wx, wy = wy, wx
           wx = wx * -1
       if i[1]==360:
           pass
    if i[0] == 'L':
        if i[1] == 90:
            wx, wy = wy, wx
            wx = wx * -1
        if i[1] == 180:
            wx = wx * -1
            wy = wy * -1
        if i[1] == 270:
            wx, wy = wy, wx
            wy = wy * -1
        if i[1] == 360:
            pass


#print(x,y)
print(abs(x)+abs(y))
