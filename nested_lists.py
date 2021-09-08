if __name__ == '__main__':
    scores = set()
    names = []
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
        scores.add(score)
    
    low_score = sorted(scores)[1]
    for n, s in l:
        if(s == low_score):
            names.append(n)
    
    for n in sorted(names):
        print(n, end='\n')
    
        
   
