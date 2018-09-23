# -*- encoding UTF-8 -*-
class Logic:
	"""
	Esta clase se encarga de definir el comportamiento predictivo,
	principalmente de la máquina y puede ayudar a predecir el del usuario
	"""
	def __init__(self, dificulty, table):
		self.dificulty = dificulty
		self.table_weight = [[0,0,0],[0,0,0],[0,0,0]]
		self.table = table
		self.sing = 4		
		

	def getWeights(self):
		"""
		Metodo encargado de definir la tabla con las mejores jugadas
		Condiciones:
			La posicion en la tabla debe ser 0
			Si se trata de un extremo, cuenta con un peso de 7
			Si está en la misma fila que otra que ya tenga, se le suma 2
			Si está en la misma diagonal 3
			Si la posición está ocupada, pasa a tener un peso negativo
		"""
		self.table_weight = [[0,0,0],[0,0,0],[0,0,0]]
		for j in range(len(self.table)):
			for i in range(len(self.table[j])):
				if self.table[j][i] == 0:
					if (j is 0 or j is 2) and (i is 0 or i is 2):
						print("entra con {},{} en 7".format(j, i))
						self.table_weight[j][i] +=7
						posj = 2 if j is 0 else 0
						posi = i
						if self.table[posj][posi] is self.sing:
							self.table_weight[j][i] +=2
						posi = 2 if i is 0 else 0
						if self.table[posj][posi] is self.sing:
							self.table_weight[j][i] +=3
						posj = j
						if self.table[posj][posi] is self.sing:
							self.table_weight[j][i] +=2		
				else:
					self.table_weight[j][i] -=1
		return self.atack()

	def atack(self):
		"""
		Función encargada de determinar cual es la posición con más puntos
		Primero evalua en que fila se encuentra. Una vez que sabe la fila,
		cual es la posición de dicha fila
		"""
		print("entramos en atack")
		rows = [max(x) for x in self.table_weight]
		print(rows)
		val = max(rows)		
		j = rows.index(val)
		i = self.table_weight[j].index(val)
		return j, i

"""a = [[4,0,0],[0,0,0],[0,0,0]]
l = Logic(1, a)
l.getWeights()"""





