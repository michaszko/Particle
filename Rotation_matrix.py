from math import cos, sin

class Matrix:
	"""Klasa macierzy obrotu zgodnie z ruchem wskazówek zegara 2x2"""

	def __init__(self, angle):
		self.matrix = [ [ -cos(angle), sin(angle) ], [ -sin(angle), -cos(angle) ] ]
			
	def __add__(self, other):
		tmp = [[0 for x in range(2)] for y in range(2)] 
	
		for i in range(2):
			for j in range(2):
				tmp[i][j] = self.matrix[i][j] + other.matrix[i][j]
			
		return Matrix(tmp)
		
		
	def __mul__(self, other):
		tmp = [[0 for x in range(2)] for y in range(2)] 
	
		for i in range(2):
			for j in range(2):
				for k in range(2):
					tmp[i][j] += self.matrix[i][k] * other.matrix[k][j]
	
		return Matrix(tmp)
	
	def transposition( self ):
		(self.matrix[1][0], self.matrix[0][1]) = (self.matrix[0][1], self.matrix[1][0])
		

