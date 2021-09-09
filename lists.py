if __name__ == '__main__':
    li = []
    N = int(input())
    for _ in range(N):
        c = input().strip().split() #important!
        if(c[0] == "insert"):
            li.insert(int(c[1]), int(c[2]));
        elif(c[0] == "append"):
            li.append(int(c[1]))
        elif(c[0] == "remove"):
            li.remove(int(c[1]))
        elif(c[0] == "print"):
            print(li)
        elif(c[0] == "sort"):
            li.sort()
        elif(c[0] == "pop"):
            li.pop()
        elif(c[0] == "reverse"):
            li.reverse()
        
