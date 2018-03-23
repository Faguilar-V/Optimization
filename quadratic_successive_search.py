#cuadraticas sucesivas

def f(x):
    global evalF
    try:
        f_x = (2.0 * (x ** 2.0)) + (16.0 / x)
        evalF += 1
    except Exception:
        f_x = 1e100
    return f_x

def x_estrellita(x_1, x_2, x_3, f_x):
    a_0 = f_x[0]
    a_1 = (f_x[1] - f_x[0]) / (x_2 - x_1)
    a_2 = (1.0 / (x_3 - x_2)) * (((f_x[2] - f_x[0]) / (x_3 - x_1)) - a_1)
    #if a_2 < 0:
    #    return x_1
    #else:
    x_estrella = ((x_1 + x_2) / 2.0) - (a_1 / (2.0 * a_2))
    return x_estrella

def polinomial(x_1, delta, epsilon):
    #calculos
    x_2 = x_1 + delta
    f_x1 = f(x_1)
    f_x2 = f(x_2)
    #obtención del x_3
    if f_x1 > f_x2:
        x_3 = x_1 + 2.0 * delta
        f_x3 = f(x3)
    else:
        x_3 = x_1 - delta
        f_x3 = f(x_3)
    #reordenamiento
    d = {x_1:f_x1, x_2:f_x2, x_3:f_x3}
    x_1, x_2, x_3 = sorted(d)
    f_x1, f_x2, f_x3 = d.get(x_1), d.get(x_2), d.get(x_3)
    f_xmin = min(d.values())
    x_min = list(d.keys())[list(d.values()).index(f_xmin)]
    f_x = [f_x1, f_x2, f_x3 ]
    #iteración
    x_b = x_estrellita(x_1, x_2, x_3, f_x)
    f_xb = f(x_b)
    #Añadimos el x_b al diccionario
    d[x_b] = f_xb
    #Reordenamos
    aux = 0
    f_x1, f_x2, f_x3 , aux = sorted(d.values())
    x_1, x_2, x_3 = list(d.keys())[list(d.values()).index(f_x1)], list(d.keys())[list(d.values()).index(f_x2)], list(d.keys())[list(d.values()).index(f_x3)]
    ###########%%%%%%%%%%%%%%%%%%%
    #print(x_1, x_2, x_3, f_x1, f_x2, f_x3, d)

    while abs(x_min - x_b) > epsilon:
        d = {x_1:f_x1, x_2:f_x2, x_3:f_x3}
        #x_min
        f_xmin = min(d.values())
        x_min = list(d.keys())[list(d.values()).index(f_xmin)]
        x_1, x_2, x_3 = sorted(d)
        f_x1, f_x2, f_x3 = d.get(x_1), d.get(x_2), d.get(x_3)
        #iteración
        f_x = [f_x1, f_x2, f_x3]
        x_b = x_estrellita(x_1, x_2, x_3, f_x)
        f_xb = f(x_b)
        #Añadimos el x_b al diccionario
        d[x_b] = f_xb
        #Reordenamos
        aux = 0
        f_x1, f_x2, f_x3 , aux = sorted(d.values())
        x_1, x_2, x_3 = list(d.keys())[list(d.values()).index(f_x1)], list(d.keys())[list(d.values()).index(f_x2)], list(d.keys())[list(d.values()).index(f_x3)]
    print('(%.3f, %.3f)' % (x_b, f_xb))
    return evalF

if __name__ == '__main__':
    evalF = 0
    x_0, delta, epsilon = map(float, input().split(','))
    print(polinomial(x_0, delta, epsilon))
    
