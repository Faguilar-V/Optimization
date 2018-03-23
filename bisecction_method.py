#Metodo de bisección

def f(X):
    try:
        f_X = (X ** 2.0) + (54.0 / X )
    except Exception:
        f_X = 1e1000
    return f_X

def f_1(x):
    global evalF
    try:
        f_x = (2.0 * x) - (54.0 / x ** 2.0)
        evalF += 1
    except Exception:
        f_x = 1e1000
    return f_x

def biseccion(a, b, eps):
    global evalF
    f_a = f_1(a)
    f_b = f_1(b)
    if f_a <= 0 and f_b >= 0:
        while True:
            z = (a + b) / 2.0
            f_z = f_1(z)
            if f_z < 0:
                a = z
            else:
                b = z
            if abs(f_z) <= eps:
                break            
    else:
        print("Error")
    print("(%.3f,%.3f)" % (z,f(z)))
    return evalF

if __name__ == '__main__':
    evalF = 0
    a, b, eps = map(float, input().split(','))
    print(biseccion(a, b, eps))
    
