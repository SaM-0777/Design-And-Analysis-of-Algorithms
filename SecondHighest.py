l = [5, 7, 0, 2, 8, 7, 4]
max = 0
second_max = 0
for i in range(len(l)):
    if l[max] < l[i]:
        max = i
    if l[second_max] < l[i] and l[second_max] < l[max]:
        second_max = i

print("Highest : {0}\nSecond Highest : {1}".format(l[max], l[second_max]))