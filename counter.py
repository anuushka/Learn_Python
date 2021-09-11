# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x = int(input())
sizes = Counter(map(int, input().split()))
n = int(input())
total = []
for i in range(n):
    size, price = map(int, input().split())
    if(sizes[size] > 0):
        total.append(price)
        sizes.subtract(Counter([size]))
    else:
        pass
print(sum(total))
    
