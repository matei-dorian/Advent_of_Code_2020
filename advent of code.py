def create_dict(p):
    d = {}

    p = p.split()
    #print(p)
    for x in p:
        poz = x.find(':')
        d[x[:poz]] = x[poz+1:]

    return d


def verify1(d):

    if len(d.keys()) == 8:
        return 1
    if len(d.keys()) == 7 and "cid" not in d.keys():
        return 1
    return 0

def verify2(d):
    if verify1(d) == 0:  # if it does not have all keys it is not good
        return 0
    for k in d.keys():   # we verify all the conditions
        if k == 'byr':
           if 1920>int(d[k]) or int(d[k])>2002:
               return 0
        if k == 'iyr':
            if 2010>int(d[k]) or int(d[k])>2020:
                return 0
        if k == 'eyr':
            if 2020>int(d[k]) or int(d[k])>2030:
                return 0
        if k == 'hgt':
            pozcm = d[k].find("cm")
            pozin = d[k].find("in")
            poz = max(pozcm,pozin)
            if poz == -1:
                return 0
            if poz == pozcm and (150>int(d[k][:pozcm]) or int(d[k][:pozcm])>193):
                return 0
            if poz == pozin and (59>int(d[k][:pozin]) or int(d[k][:pozin])>76):
                return 0
        if k == 'hcl':
            if len(d[k]) != 7:
                return 0
            if d[k].find('#') == -1:
                return 0
            for x in d[k][d[k].find('#')+1:]:
                if x.isdigit() is False and ('a'>x or x>'f'):
                    return 0
        if k == 'ecl':
            if d[k] not in {"amb","blu", "brn","gry","grn","hzl","oth"}:
                return 0
        if k == 'pid':
            if len(d[k]) != 9:
                return 0
            for x in d[k]:
                if x.isdigit() is False:
                    return 0
    return 1

f = open("Input")
L = f.read().split("\n\n")

ct1 = 0  # number of valid passports in task 1
ct2 = 0  # number of valid passports in task 2

for i in L:
    d = create_dict(i)  # we create a dictionary for each passport
    #print(d)
    if verify1(d) == 1:
        ct1 += 1  # for task 1
    if verify2(d) == 1:
        ct2 += 1  # for task 2

print(ct1)
print(ct2)
exit()
