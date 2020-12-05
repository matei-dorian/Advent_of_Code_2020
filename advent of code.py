def Valid1(x):
    # here I used the particular form of the input to extract all the needed data
    lwb = int(x[:x.find('-')])  # the lowest number of times a character can appear is the first number
    upb = int(x[x.find('-') + 1:x.find(' ')])  # the highest number of times a character can appear is the second number
    c = x[x.find(' ') + 1]  # the character that needs to be counted
    password = x[x.find(':') + 2:]
    nr = password.count(c)
    if lwb <= nr <= upb:
        return 1
    return 0


def Valid2(x):
    # same thing as in the first task but the condition is changed
    lwb = int(x[:x.find('-')])
    upb = int(x[x.find('-') + 1:x.find(' ')])
    c = x[x.find(' ') + 1]
    password = x[x.find(':') + 2:]

    ct = 0
    if password[lwb - 1] == c:
        ct += 1

    if password[upb - 1] == c:
        ct += 1

    if ct == 1:
        return 1
    else:
        return 0


f = open("Input")
L = [x for x in f.readlines()]  # created list using list comprehension

# first task
ct1 = 0  # number of valid passwords
for x in L:
    if Valid1(x):
        ct1 += 1

# second task
ct2 = 0  # number of valid passwords
for x in L:
    if Valid2(x):
        ct2 += 1
print(ct1)
print(ct2)
exit()

# the complexity of the Valid1 and Valid2 functions is O(lenght of password)
# the complexity of the programme is O(n*lengt of password)
