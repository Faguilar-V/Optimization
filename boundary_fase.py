#!/usr/bin/python

def f(x):
    global evalF
    f_x = (100.0 - x) ** 2.0
    evalF += 1
    return f_x

if __name__ == '__main__':
    x_0, delta = map(float, input().split(','))
    evalF = 0
    aux = False
    array_X = [x_0 - abs(delta), x_0, x_0 + abs(delta)]
    f_x  = [f(array_X[0]), f(array_X[1]), f(array_X[2])]
    #Gradient + or  -
    if  f_x[0] >= f_x[1] >= f_x[2]:
        delta = abs(delta)
        x_1 = x_0 + delta
        array_X.append(x_1)
    else:
        if f_x[0] <= f_x[1] <= f_x[2]:
            delta = abs(delta) * -1
            x_1 =  x_0 + delta
            array_X.append(x_1)
        else:
            aux = True
            print("(%.3f,%.3f)" %(array_X[-3],array_X[-1]))
            print(evalF)
    while True:
        if aux == False:
            k = 1
            aux = 0
            x_2 = array_X[-1] + ((2.0 ** k) * delta)
            array_X.append(x_2)
            f_x.append(f(array_X[-1]))
            while f_x[-1] < f_x[-2]:
                k += 1
                array_X.append(array_X[-1] + ((2.0 ** k) * delta))
                f_x.append(f(array_X[-1]))
            print("(%.3f,%.3f)" %(array_X[-3],array_X[-1]))
            print(evalF)
            break
        else:
            break
    
