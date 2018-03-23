#Newthon rapson method
def f(x):
    try:
        f_x = x ** 2 + 54 / x
    except Exception:
        f_x = 1e1000
    return f_x

def f1(x):
    global evalF
    f_x = 2.0 * x - 54.0 / x ** 2.0
    evalF += 1
    return f_x

def f2(x):
    f_x = 2.0 + 108.0 / x ** 3.0
    return f_x

def newton_raph(x, epsilon):
    arr_x = [f1(x), f2(x)]
    while True:
        x_k = x - (arr_x[-2] / arr_x[-1])
        arr_x[-2] = f1(x_k)
        if abs(arr_x[-2]) <=  epsilon:
            break
        else:
            x = x_k
            arr_x[-1] = f2(x)
            continue
    print('(%.3f,%.3f)' % (x_k, f(x_k)))
    return evalF

if __name__ == '__main__':
    evalF = 0
    x, epsilon = map(float, input().split(','))
    print(newton_raph(x, epsilon))

