k,li = int(input()),list(map(int, input().split()))

s = set(li)

print(((sum(s)*k)-(sum(li)))//(k-1))
