import copy


def get_first_seat(point):
    x, y = point
    count_list = []

    x_val = x +1
    y_val = y
    #right
    while 0 <= y_val <= len(G) -1 and 0 <= x_val <= len(G[0]) - 1:
        if G[y][x_val] in ["L","#"]:
            if G[y][x_val] == "L":
                break
            elif G[y][x_val] == "#":
                count_list.append(1)
                break
        x_val += 1

    x_val = x - 1
    y_val = y
    #left
    while 0 <= y_val <= len(G) - 1 and 0 <= x_val <= len(G[0]) - 1:
        if G[y][x_val] in ["L","#"]:
            if G[y][x_val] == "L":
                break
            elif G[y][x_val] == "#":
                count_list.append(1)
                break
        x_val -= 1

    x_val = x
    y_val = y - 1
    #up
    while 0 <= y_val <= len(G) -1 and 0 <= x_val <= len(G[0]) - 1:
        if G[y_val][x] in ["L","#"]:
            if G[y_val][x] == "L":
                break
            elif G[y_val][x] == "#":
                count_list.append(1)
                break
        y_val -= 1

    x_val = x
    y_val = y + 1

    #down
    while 0 <= y_val <= len(G) -1 and 0 <= x_val <= len(G[0]) - 1:
        if G[y_val][x] in ["L","#"]:
            if G[y_val][x] == "L":
                break
            elif G[y_val][x] == "#":
                count_list.append(1)
                break
        y_val += 1

    #leftdown
    x_val = x - 1
    y_val = y + 1
    while 0 <= y_val <= len(G) -1 and 0 <= x_val <= len(G[0]) - 1:
        if G[y_val][x_val] in ["L","#"]:
            if G[y_val][x_val] == "L":
                break
            elif G[y_val][x_val] == "#":
                count_list.append(1)
                break
        y_val += 1
        x_val -= 1

    #rightdown
    x_val = x + 1
    y_val = y + 1
    while 0 <= y_val <= len(G) -1 and 0 <= x_val <= len(G[0]) - 1:
        if G[y_val][x_val] in ["L","#"]:
            if G[y_val][x_val] == "L":
                break
            elif G[y_val][x_val] == "#":
                count_list.append(1)
                break
        y_val += 1
        x_val += 1

    #rightup
    x_val = x + 1
    y_val = y - 1
    while 0 <= y_val <= len(G) -1 and 0 <= x_val <= len(G[0]) - 1:
        if G[y_val][x_val] in ["L","#"]:
            if G[y_val][x_val] == "L":
                break
            elif G[y_val][x_val] == "#":
                count_list.append(1)
                break
        y_val -= 1
        x_val += 1

    #leftup
    x_val = x - 1
    y_val = y - 1
    while 0 <= y_val <= len(G) - 1 and 0 <= x_val <= len(G[0]) - 1:
        if G[y_val][x_val] in ["L", "#"]:
            if G[y_val][x_val] == "L":
                break
            elif G[y_val][x_val] == "#":
                count_list.append(1)
                break
        y_val -= 1
        x_val -= 1

    return sum(count_list)


# create a list of the adjacent points
def adj_points(point):
    x, y = point
    return [(x + 1, y), (x - 1, y), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1), (x, y + 1),
            (x, y - 1)]




# task 1
f = open("Input")
G = [list(i.strip('\n')) for i in f.readlines()]  # initial grid
#
# for i in range(len(G)):
#     print(G[i])

# NewG = copy.deepcopy(G)
# cts = 0  # number of occupied seats
# while True:
#     for i in range(len(G)):
#         for j in range(len(G[0])):  # iterate through the grid
#             x = G[i][j]  # we are at G[i][j]
#             if x != '.':  # if there is a seat
#                 list_of_points = adj_points((i, j))
#                 ct = 0
#                 for v in list_of_points:  # generating the adjacent positions
#                     iv = v[0]
#                     jv = v[1]
#                     if 0 <= iv <= len(G) - 1 and 0 <= jv <= len(G[0]) - 1:  # check if the position is in the grid
#                         if G[iv][jv] == '#':
#                             ct += 1
#                 # we apply the rules
#                 if x == '#' and ct >= 4:
#                     NewG[i][j] = 'L'
#                 if x == 'L' and ct == 0:
#                     NewG[i][j] = '#'
#     # if the resulted grids are equal we stop before we loop
#     if NewG == G:
#         for lin in NewG:
#             cts += lin.count("#")
#         break
#     G = copy.deepcopy(NewG)  # switching the grids
#
# print(cts)
#
# # task 2
# f = open("Input")
# G = [list(i.strip('\n')) for i in f.readlines()]  # initial grid
#
# for i in range(len(G)):
#     print(G[i])

NewG = copy.deepcopy(G)
cts = 0  # number of occupied seats
while True:
    for i in range(len(G)):
        for j in range(len(G[0])):  # iterate through the grid
            x = G[i][j]  # we are at G[i][j]
            if x != '.':  # if there is a seat
                #list_of_points = adj_points((i, j))
                ct = get_first_seat((j,i))
                # we apply the rules
                if x == '#' and ct >= 5:
                    NewG[i][j] = 'L'
                if x == 'L' and ct == 0:
                    NewG[i][j] = '#'
    # if the resulted grids are equal we stop before we loop
    if NewG == G:
        for lin in NewG:
            cts += lin.count("#")
        break
    G = copy.deepcopy(NewG)  # switching the grids

print(cts)
