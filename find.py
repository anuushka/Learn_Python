def count_substring(string, sub_string):
    k = 0
    for _ in range(len(string)):
        i = string.find(sub_string)
        while( i != -1):
            k+=1
            i = string.find(sub_string, i+1)
        return k

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
