x = [0, 45, 12, 63, 21, 8, 102]
print(len(x))

y = int(len(x) / 2)
z = x[:1]
print(y)
print(x[:y])
print(x[y:])
print(len(z))