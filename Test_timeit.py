import timeit

def func(c):
    print(c)

t = timeit.timeit(lambda : func(5), number = 1000)

print("T : ", t)