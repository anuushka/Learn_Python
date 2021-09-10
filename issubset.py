t = int(input())
for _ in range(t):
    na = int(input())
    a = set(map(int, input().split()))
    nb = int(input())
    b = set(map(int, input().split()))
    print(a.issubset(b))
