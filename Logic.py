# -*- encoding UTF-8 -*-
from Matrix import Matrix

from random import randint


class Logic(Matrix):
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
			Si hay una combinación que pueda ganar, tendrá un peso de 14
			Si se trata de un extremo, cuenta con un peso de 7
			Si está en la misma fila que otra que ya tenga, se le suma 2
			Si está en la misma diagonal 3
			Si la posición está ocupada, pasa a tener un peso negativo
		"""		
		self.table_weight = [[0,0,0],[0,0,0],[0,0,0]]
		values = self.sum()		
		if self.sing*2 in values or 2 in values:
			try:
				p = values.index(self.sing*2)
			except:
				p = values.index(2)
			if p <3:
				j = p
				i = self.table[j].index(0)
			elif 3<=p<6:
				i = p-3
				j = self.matrix_t[i].index(0)
				input("({}, {})".format(j, i))
			elif p is 6:
				i = j = self.d1.index(0)
			else:
				j = self.d2.index(0)
				i = -j-1
			self.table_weight[j][i] +=14
			input(self.table_weight)
			return self.atack()

		for j in range(len(self.table)):
			for i in range(len(self.table[j])):
				if self.table[j][i] == 0:
					if (j is 0 or j is 2) and (i is 0 or i is 2):
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

		weights = list(self.flat(self.table_weight))
		mx = max(weights)
		repetitions = len(list(filter(lambda x: x is mx, weights)))
		if repetitions >1:
			opts = list(self.searchFor(self.table_weight, mx, 2))			
			j, i = opts[randint(0, len(opts))]
		else:
			p = weights.index(mx)
			j = int(p/3)
			i = p%3
		print(j, i)

		"""
		rows = [max(x) for x in weights]
		val = max(rows)		
		j = rows.index(val)
		i = self.table_weight[j].index(val)
		"""
		return j, i