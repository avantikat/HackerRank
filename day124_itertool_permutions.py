from itertools import permutations
str, num = input().split(" ")
permutations = list(permutations(str, int(num)))
permutations.sort()

[print("".join(i)) for i in permutations]
