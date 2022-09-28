def recursive_binomial(n, k):
    if n == k:
        return 1
    elif k == 0:
        return 1
    
    return recursive_binomial(n-1, k) + recursive_binomial(n-1, k-1)


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    if n > k and k >= 1:
        print(recursive_binomial(n, k))