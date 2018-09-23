from functools import reduce
class Matrix:
	"""En esta clase se almacenan todas las acciones en lo referente a la matriz, desde su creación
	hasta su manipulación como su analisis"""
	def __init__(self):
		self.table = [[0,0,0],[0,0,0],[0,0,0]]
		self.matrix_t = [[0,0,0],[0,0,0],[0,0,0]]
		self.d1 = [0,0,0]
		self.d2 = [0,0,0]

	#Generadores
	def flat(self, l):
		for j in range(len(l)):
			for i in range(len(l[j])):
				yield l[j][i]

	def searchFor(self, l, field, dimensions = 2):
		"""
		metdo encargado de buscar un valor en una matriz y devolver todas las posiciones en las que se encuentra
		"""
		n = field
		if dimensions is 1:
			for i in range(len(l)):
				if l[i] is n:
					yield i
		elif dimensions is 2:
			for j in range(len(l)):
				for i in range(len(l[j])):
					if l[j][i] is n:
						yield j, i


	def getCombine(self):
		return [self.table, self.transpuest(self.table), self.getDiagonal(self.table)]

	def transpuest(self, matrix):
		m = []
		for i in range(len(matrix[0])):
			m.append([])
			for h in range(len(matrix)):
				m[-1].append(matrix[h][i])
		self.matrix_t = m
		return m

	def getDiagonal(self, matrix):
		d1, d2 = [], []
		for j in range(len(matrix)):
			d1.append(matrix[j][j])
			d2.append(matrix[j][-j-1])
		self.d1 = d1
		self.d2 = d2
		return [d1, d2]

	def sum(self):
		"""
		Este metodo se encarga de analizar la matriz y devolver un array con la suma de todas las
		combinaciones de 3 posibles
		"""
		the_sum = []
		tables = self.getCombine()
		zeros, iterations = 0, 0
		for j in tables:
			for i in j:
				iterations+=1
				a = [p for p in i]
				the_sum.append(reduce(lambda x, y : x+y, a))
				if 0 not in a:
					zeros+=1
		return the_sum if zeros != iterations else False		
