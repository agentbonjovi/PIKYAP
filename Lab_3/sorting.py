data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

print(1)
print(sorted(data, key = lambda x: abs(x), reverse = True))

print(2)
def sort_key(x): return abs(x)
print(list(sorted(data, key = sort_key, reverse = True)))