n = int(input())
a = set(map(int, input().split()))
N = int(input())
for i in range(N):
    c, length = input().split()
    b  = set(map(int, input().split()))
    if(c == "intersection_update"):
        a.intersection_update(b)
    elif(c == "update"):
        a.update(b)
    elif(c == "symmetric_difference_update"):
        a.symmetric_difference_update(b)
    elif(c == "difference_update"):
        a.difference_update(b)
print(sum(a))
