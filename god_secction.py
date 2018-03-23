
def f(x):
    global evalF
    f_x = (100 - x) ** 2
    evalF += 1
    return f_x

def fw(w):
    global a, b
    x = (w * (b - a)) + a
    return x

def gold_section(a, b, epsilon):
    umbral = epsilon / (b - a)
    a_w, b_w = 0, 1
    L_w = b_w - a_w
    flag = 0
    while L_w > umbral:
        if flag == 0:
            w_1 = a_w + 0.618 * L_w
            w_2 = b_w - 0.618 * L_w
            w_n1 = fw(w_1)
            w_n2 = fw(w_2)
            f_w1 = f(w_n1)
            f_w2 = f(w_n2)
        else:
            if flag == 1:
                w_1 = a_w + 0.618 * L_w
                w_n1 = fw(w_1)
                f_w1 = f(w_n1)
            else:
                w_2 = b_w - 0.618 * L_w
                w_n2 = fw(w_2)
                f_w2 = f(w_n2)
        if f_w1 < f_w2:
            a_w = w_2
            w_2 = w_1
            w_n2 = w_n1
            f_w2 = f_w1
            flag = 1
        else:
            if f_w1 > f_w2:
                b_w = w_1
                w_1 = w_2
                w_n1 = w_n2
                f_w1 = f_w2
                flag = 2
            else:
                a_w, b_w = w_1, w_2
                flag = 0
        L_w = b_w - a_w
    print('(%.3f,%.3f)' % (fw(a_w), fw(b_w)))
    return evalF

if __name__ == '__main__':
    evalF = 0
    a, b, epsilon = map(float, input().split(','))
    print(gold_section(a, b, epsilon))
