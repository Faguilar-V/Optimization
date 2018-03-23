#!/usr/bin/python3

def f(x):
    global evalF
    f_x = x ** 2.0 + (54.0 / (x + 10.0))
    evalF += 1
    return f_x

def half_intervals(a, b, epsilon):
    x_m = (b + a) / 2.
    L = b - a
    #x_m
    arr_x_m = [x_m]
    arr_f_x_m = [f(arr_x_m[0])]
    arr_x = [a, b]
    arr_f_x = [a, b]
    #iter
    while abs(L) > epsilon:
        x_1 = a + (L / 4.)
        x_2 = b - (L / 4.)
        #print(a, b)
        arr_x[0] = x_1
        arr_x[1] = x_2
        #print(arr_x)
        arr_f_x[0] = f(arr_x[0])
        arr_f_x[1] = f(arr_x[1])
        #print(arrf_x)
        if arr_f_x[0] < arr_f_x_m[0]:
            b = arr_x_m[0]
            x_m = arr_x[0]
            arr_x_m[0] = x_m
            arr_f_x_m[0] = arr_f_x[0]

        elif arr_f_x[1] < arr_f_x_m[0]:
            a = arr_x_m[0]
            x_m = arr_x[1]
            arr_x_m[0] = x_m
            arr_f_x_m[0] = arr_f_x[1]

        else:
            a = arr_x[0]
            b = arr_x[1]
        L = b - a
        #Evaluations
        #print(arr_x, arr_f_x, arr_x_m, arr_f_x_m, L)
        #print("\n")
    print('(%.3f,%.3f)' %  (a, b))
    return evalF

if __name__ == '__main__':
    evalF = 0
    a, b, epsilon = map(float, input().split(','))
    print(half_intervals(a, b, epsilon))
