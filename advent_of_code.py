# # task 1
# f = open("Input")
# n = int(f.readline().strip('\n'))
# L = [int(x) for x in f.read().split(',') if x != 'x']
# print(L)
# minwait = 10000000000
# ID = -1
# for i in L:
#     t = i
#     while t<=n:
#         t = t + i
#     #print(t)
#
#     wait = t - n
#
#     if wait < minwait:
#        minwait = wait
#        ID = i


# print(minwait*ID)
f = open('Input').read().split('\n')
f = f[1].split(',')
B = [(int(f[k]), k) for k in range(len(f)) if f[k] != 'x']

lcm = 1
time = 0
for i in range(len(B) - 1):
    bus_id = B[i + 1][0]
    idx = B[i + 1][1]
    lcm *= B[i][0]
    while (time + idx) % bus_id != 0:
        time += lcm
print(time)
