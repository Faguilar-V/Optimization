#!/usr/bin/python3
#Cuasi Newthon
"""
Fernando Rodrigo Aguilar Javier
# Copyright (C) 2018
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
#Author: Fernando Rodrigo Aguilar Javier
#Author email: faguilar@comunidad.unam.mx
#
#Details
--------------------------------------------------------------------
#
"""
##########################%%%%%%%%%%%%%%%%%%%%################################
def f(X):
    global evalF
    try:
        f_X = (X ** 2.0) + (54.0 / X)
        evalF += 1
    except Exception:
        f_X = 1e1000
    return f_X


def f1(x, arr):
    global delta
    try:
        f1_x = (arr[-2] - arr[-1]) / (2 * delta)
    except Exception:
        f1_x = 1e1000
    return f1_x


def f2(x, arr):
    global delta
    try:
        f2_x = (arr[-2] - 2 * f(x) + arr[-1]) / delta ** 2.0
    except Exception:
        f2_x = 1e1000
    return f2_x


def cuasi_newthon(x, epsilon, delta):
    arr = [f(x + delta), f(x - delta)]
    while True:
        arr_x = [f1(x, arr), f2(x, arr)]
        x_k = x - (arr_x[-2] / arr_x[-1])
        arr = [f(x_k + delta), f(x_k - delta)]
        arr_x[-2] = f1(x_k, arr)
        if abs(arr_x[-2]) <= epsilon:
            break
        else:
            x = x_k
            continue
    print('(%.3f,%.3f)' % (x_k, f(x_k)))
    return evalF


if __name__ == '__main__':
    evalF = 0
    x, epsilon, delta = map(float, input().split(','))
    print(cuasi_newthon(x, epsilon, delta))
