from itertools import permutations
s, k = input().split()
p = sorted(list(permutations(s, int(k))))
for i in p:
    print("".join(i))
