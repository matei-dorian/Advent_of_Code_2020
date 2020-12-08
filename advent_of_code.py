def add_dict(x, d):
    x = x.split()
    k = ""
    for i in range(len(x)):

        if x[i].find("bag") != -1:
            cuv = x[i - 2] + " " + x[i - 1]

            if k == "":
                k = cuv
                d[k] = []
            elif cuv != "no other":
                d[k].append([int(x[i-3]),cuv])
    return d

def search(bag):
    for k in d.keys():
        #print(d[k])
        for v in d[k]:
            if bag == v[1]:
                #print(bag)
                list_bags.add(k)     # we found a bag that can contain our initial searched bag
                search(k)  # we search for every bag that can hold the found bag


def count_bags(bag):
    nr = 1
    for v in d[bag]:
        print(v)
        nr += v[0]*count_bags(v[1])
    return nr

f = open("Input")
L = [x.strip() for x in f.readlines()]
d = {}
for line in L:
    add_dict(line, d)
ct = 0
list_bags = set()

search("shiny gold")
print(len(list_bags))

nr= count_bags("shiny gold")
print(nr-1)
#print(L)
#print(d)
