class Prueba(object):
	def __init__(self):
		self.__privado = 'soy privado'
		self.privado = 'soy publico'

	def __metodoPrivado(self):
		return "soy privado"

	def metodoPublico(self):
		return 'soy publico'

	def getPrivado(self):
		return self.__privado

	def setPrivado(self, valor):
		self.__privado = self.__metodoPrivado()


obj = Prueba()
## prints
obj.setPrivado("Tengo nuevo valor")
print obj.getPrivado()