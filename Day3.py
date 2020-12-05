def go_through(step1, step2):
    ct = 0
    lin = 0
    col = 0  # we are in L[0][0]

    while lin < n:
        if L[lin][col] == 1:
            ct += 1
        lin += step1
        col += step2
        if col >= m - 1:
            col = col % (m - 1)
    return ct


f = open("Input")
L = [[1 if x == '#' else 0 for x in line] for line in f.readlines()]  # created the matrix using list comprehension
# each element was coded as 1 for '#" and 0 for '.'
print(L)

# first task
ct = 0         # number of trees (1 in the matrix) encountered
n = len(L)     # number of lines
m = len(L[0])  # number of columns
lin = 0
col = 0        # we are in L[0][0]

while lin < n:
    if L[lin][col] == 1:
        ct += 1
    lin += 1
    col += 3
    if col >= m - 1:
        col = col % (m - 1)

print(ct)

# second task
# we will define a function that does the same thing but with diffrent steps
print(ct * go_through(1, 1) * go_through(1, 5) * go_through(1, 7) * go_through(2, 1))
