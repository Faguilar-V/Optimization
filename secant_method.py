#!/usr/bin/python3
#Secante method
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
##########################%%%%%%%%%%%%%%%%%%%%###############################

# Metodo de bisección

def f(X):
    try:
        f_X = (X ** 2.0) + (54.0 / X)
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


def biseccion(X_L, X_R, eps):
    flag = 0
    f_XL = f_1(X_L)
    f_XR = f_1(X_R)
    f_z = 0
    if f_XL * f_XR < 0:
        while True:
            z = X_R - ((f_XR * (X_R - X_L)) / (f_XR - f_XL))
            f_z = f_1(z)
            if f_z < 0:
                X_L = z
                f_XL = f_z
                flag = 0
            else:
                X_R = z
                f_XR = f_z
                flag = 1
            if abs(f_z) <= eps:
                break
    else:
        print("Error")
    print("(%.3f,%.3f)" % (z, f(z)))
    return evalF


if __name__ == '__main__':
    evalF = 0
    X_L, X_R, eps = map(float, input().split(','))
    print(biseccion(X_L, X_R, eps))
