x = 0

def recursive_binomial(n, k, values):
    global x 
    x += 1

    if n == k:
        return 1
    elif k == 0:
        return 1
    
    if values[n-1][k-1] == 0:
        if values[n-2][k-1] != 0:
            res1 = values[n-2][k-1]
        else:
            res1 = recursive_binomial(n-1, k, values)
        if values[n-2][k-2] != 0:
            res2 = values[n-2][k-2]
        else:
            res2 = recursive_binomial(n-1, k-1, values)
        values[n-1][k-1] =  res1 + res2
    
    return values[n-1][k-1]


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    values = [[0 for col in range(k)] for row in range(n)]    #array filled with zeros to store the values
    if n > k and k >= 1:
        print(recursive_binomial(n, k, values))
        print(x)