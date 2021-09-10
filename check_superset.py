a = set(map(int, input().split()))
n = int(input())
bool_li = []
for _ in range(n):
    b = set(map(int, input().split()))
    if(a.issuperset(b)):
        bool_li.append(True)
    else:
        bool_li.append(False)
print(all(bool_li))
