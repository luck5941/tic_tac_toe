from functools import reduce
class Matrix:
	"""En esta clase se almacenan todas las acciones en lo referente a la matriz, desde su creación
	hasta su manipulación como su analisis"""
	def __init__(self):
		self.table = [[0,0,0],[0,0,0],[0,0,0]]

	def getCombine(self):
		return [self.table, self.transpuest(self.table), self.getDiagonal(self.table)]

	def transpuest(self, matrix):
		m = []
		for i in range(len(matrix[0])):
			m.append([])
			for h in range(len(matrix)):
				m[-1].append(matrix[h][i])
		return m

	def getDiagonal(self, matrix):
		d1, d2 = [], []
		for j in range(len(matrix)):
			d1.append(matrix[j][j])
			d2.append(matrix[j][-j-1])
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
		print(iterations, zeros)
		return the_sum if zeros != iterations else False
				

		
		"""
		tables = [self.table, self.transpuest(self.table), self.getDiagonal(self.table)]
		for j in tables:
			for i in j:
				a = [p for p in i]
				if all(i == a[0] and i is not 0 for i in a):                   
				   return True
		return  False
		"""