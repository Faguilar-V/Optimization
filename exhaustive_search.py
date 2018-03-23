#!/usr/bin/python
# Enter your code here. Read input from STDIN. Print output to STDOUT
#Exhaustive algorithm

def f(x):
    global evalF
    try:
        f_x = x ** 2 + 54 / x
        evalF += 1
    except Exception:
        f_x = 1e1000
    return f_x

def search_exhaus(a, b, n):
    x_1 = a
    delta_x = (b - a) / n
    x_2 = x_1 + delta_x
    x_3 = x_2 + delta_x
    arr_X = [x_1, x_2, x_3]
    f_x = [f(arr_X[-3]), f(arr_X[-2]), f(arr_X[-1])]
    aux = 0
    while arr_X[2] <= b:
        if f_x[0] >= f_x[1] <= f_x[2]:
            arr_X[0], arr_X[1] = x_1, x_3
            break
        else:
            aux_x2, aux_x3 = arr_X[1], arr_X[2]
            arr_X[0] = aux_x2
            arr_X[1] = aux_x3
            arr_X[2] = aux_x3 + delta_x
            aux_x2, aux_x3 = f_x[1], f_x[2]
            f_x[0] = aux_x2
            f_x[1] = aux_x3
            f_x[2] = f(arr_X[2])
            aux = arr_X[0]
    print(('(%.3f,%.3f)') % (aux, arr_X[2]))
    print(evalF)
    return 0

if __name__ == '__main__':
    a, b, n = map(float, raw_input().split(','))
    evalF = 0
    arr = search_exhaus(a, b, n)
    #print '(' + "%.3f" % a + ',' + "%.3f" % b + ')'
    
