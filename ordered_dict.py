from collections import OrderedDict

n = int(input())
d = OrderedDict()
for i in range (n):
    item = input().split(' ')
    price = int(item[-1])
    item_name = " ".join(item[:-1])
    if(d.get(item_name)):
        d[item_name] += price
    else:
        d[item_name] = price
    
for i,v in d.items():
    print(i, v)

