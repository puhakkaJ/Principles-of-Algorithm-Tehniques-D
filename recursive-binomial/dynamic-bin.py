def recursive_binomial(n, k, values):
    if n == k:
        return 1
    elif k == 0:
        return 1
    
    if values[n-1][k-1] == 0:
        values[n-1][k-1] = recursive_binomial(n-1, k, values) + recursive_binomial(n-1, k-1, values)
    
    return values[n-1][k-1]


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    values = [[0 for col in range(k)] for row in range(n)]    #array filled with zeros to store the values
    if n > k and k >= 1:
        print(recursive_binomial(n, k, values))