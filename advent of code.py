f = open("Input")
L = {int(x) for x in f.readlines()}  # created a set using list comprehension with all the numbers in the input

# task 1
# we go through the numebrs in L and if we also find the other number we print the result
# if the current number is x then the wanted number would be 2020 - x
# complexity O(n) where n is the number of numbers in the Input file

for x in L:
    y = 2020 - x
    if y in L:
        print(y * x)
        break

# task 2
# this time we use want x+y+z=2020
# we will use 2 for loops to fixate x and y and we will verify if z = 2020 - x - y is in L
# complexity O(n^2)

for x in L:
    for y in L:
        if y != x:
            z = 2020 - y - x
            if z in L:
                print(x * y * z)
                exit()
