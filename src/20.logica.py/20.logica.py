#
#
def unico(strN):
	result = []
	arreglo = strN.split(" ")
	for el in arreglo:
		if arreglo.count(el) > 1:
			result.append(el)
	return result

print(unico("1 2 2 6 8 6 1"))
