import math

def matrix_multiplication(matrix1, matrix2):
    result = [[0 ,0], [0, 0]]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j] #integer multiplication
    
    return result


def recursive_power(base, n):
    if n == 0:
        return [[1, 0], [0, 1]] #identity matrix
    elif n == 1:
        return base
    else:
        if (n % 2 == 0):
            pow1 = recursive_power(base, n/2)
            pow2 = recursive_power(base, n/2)
        else:
            pow1 = recursive_power(base, math.ceil(n/2)) 
            pow2 = recursive_power(base, (n-math.ceil(n/2)))
        return matrix_multiplication(pow1,pow2) 


def nth_fibonacci(n):
    base = [[1, 1],[1, 0]]
    return matrix_multiplication(recursive_power(base, n - 2), [[1],[1]])


if __name__ == '__main__':
    n = int(input())
    if n >= 2:
        fib = nth_fibonacci(n)
        print("F(n) is ", fib[0][0])
        print("F(n-1) is ", fib[1][0])