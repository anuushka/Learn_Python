def average(array):
    arr = set(array)
    avg = sum(arr)/len(arr)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
