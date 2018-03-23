#!/usr/bin/python
#Fernando Rodrigo Aguilar Javier
#el fibo

def fibonacci(n):
    a, b = 1, 1
    fibo = [a, b]
    for i in range(int(n - 1)):
        fibo.append(float(a + b))
        a = b
        b = fibo[-1]
    return fibo

def f(x):
    global evalF
    try:
        f_x = x ** 2.0 + (54.0 / x)
        evalF += 1
    except Exception:
        f_x = 1e1000
    return f_x

def fib_search(a, b, n):
    n = int(n)
    L = b - a
    k = 2
    arr_fib = fibonacci(n)
    arr_f_x = [0, 1]
    flag = 2
    while k <= n:
        L_k = (arr_fib[n - k] / arr_fib[n]) * L
        #############Flags##########################
        if flag == 2:
            x_1 = a + L_k
            x_2 = b - L_k
            arr_f_x[0] = f(x_1)
            arr_f_x[1] = f(x_2)
        elif flag == 1:
            x_2 = b - L_k
            arr_f_x[1] = f(x_2)
        elif flag == 0:
            x_1 = a + L_k
            arr_f_x[0]  = f(x_1)
    
        if arr_f_x[0] > arr_f_x[1]:
            a = x_1
            x_1 = x_2
            arr_f_x[0] = arr_f_x[1]
            flag = 1
        elif arr_f_x[0] < arr_f_x[1]:
            b = x_2
            x_2 = x_1
            arr_f_x[1] = arr_f_x[0]
            flag = 0
        else:
            a, b = x_1, x_2
            flag = 2
        k += 1
    print("(%.3f,%.3f)" % (a, b))
    return evalF

if __name__ == '__main__':
    evalF = 0
    a, b, n = map(float, input().split(','))
    print(fib_search(a, b, n))
