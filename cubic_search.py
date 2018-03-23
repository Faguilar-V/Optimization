
def f(x):
	global evalF
	f_x =  (x ** 5) - (5 * (x ** 3)) - (20 * x) + 5
	evalF += 1
	return f_x

def df(x):
	global evaldF
	df_x = (5 * (x ** 4)) - (15 * (x ** 2)) - 20
	evaldF += 1
	return df_x

def x_estrella(x_1, x_2, arr_f, arr_df):
	z = ((3.0 * (arr_f[0] - arr_f[1])) / (x_2 - x_1)) + arr_df[0] + arr_df[1]
	if x_1 < x_2:
		w =  (z ** 2 - (arr_df[0] * arr_df[1])) ** .5
	else:
		w = -1 * ((z ** 2 - (arr_df[0] * arr_df[1])) ** .5)
	miu = (arr_df[1] + w - z) / (arr_df[1] - arr_df[0] + 2.0 * w)
	#condciones
	if miu < 0:
		x_estrellita = x_2
	elif 0 <= miu <= 1:
		x_estrellita = x_2 - miu * (x_2 - x_1)
	else:
		x_estrellita = x_1
	return x_estrellita


def cubical_search(x_0, delta, eps1, eps2):
	k = 0
	x_1, x_2 = 0, 0
	arr_f = [0, 0, 0]
	arr_df = [0, 0, 0]
	#Para ver hacia donde te vas a mover
	if df(x_0) > 0:
		delta *= -1
	#Para ver que todos sean positivos
	arr_df[0] = df(x_0)
	while True:
		x_k1 = x_0 + ((2 ** k) * delta)
		k += 1
		arr_df[1] = df(x_k1)
		if arr_df[0] * arr_df[1] <= 0:
			x_1, x_2 = x_0, x_k1
			break
		else:
			x_0 = x_k1
			arr_df[0] = arr_df[1]
	arr_f[0] = f(x_1)
	arr_f[1] = f(x_2)
	#sacamos el valor de x_estrella
	while True:
		x_b = x_estrella(x_1, x_2, arr_f, arr_df)
		arr_f[2] = f(x_b)
		if abs((x_b - x_1) / x_b) <= eps2:
			break
		while arr_f[2] >= arr_f[0]:
			x_b -= .5 * (x_b - x_1)
			arr_f[2] = f(x_b)
		arr_df[2] = df(x_b)
		if abs(arr_df[2]) <= eps1:
			break
		if arr_df[2] * arr_df[0] < 0:
			x_2 = x_b
			arr_f[1] = arr_f[2]
			arr_df[1] = arr_df[2]
		else:
			x_1 = x_b
			arr_f[0] = arr_f[2]
			arr_df[0] = arr_df[2]
		#print(x_1, x_2)
	print('(%.3f,%.3f)' % (x_b, arr_f[2]))
	print(evalF)
	return evaldF

if __name__ == '__main__':
	evalF = 4
	evaldF = -1
	#Inputs
	x_0, delta, eps1, eps2 = map(float, input().split(','))
	print(cubical_search(x_0, delta, eps1, eps2))
