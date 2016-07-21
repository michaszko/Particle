from math import sqrt, acos

def angle( v1, v2 ):
	"""Zwraca kąt pomiedzy dwoma wektorami"""
	return(acos( v1 * v2 / ( v1.norm() * v2.norm() ) ))
	
def cosinus( v1, v2 ):
	"""Zwraca cosinus kąta między dwoma wektorami"""
	return( v1 * v2 / ( v1.norm() * v2.norm() ) )
	
class Vector( object ):
	"""Klasa 2-wymiarowych wektorów"""
	
	def __init__( self, *args ):
		"""Tworzy nowy wektor o wartościach (x, y)"""            
		self.xy = args
		
	def __repr__( self ):
		"""Rzutowanie na string"""
		return "({0} , {1})".format(self.xy[0], self.xy[1])
	
	@classmethod	
	def from_points( cls, P1, P2 ):
		"""Zwraca wektor z punktu P2 do P1"""
		return cls( P2[0] - P1[0], P2[1] - P1[1] )
	
	@classmethod
	def matrix_mult( cls, matrix, vector):
		"""Zwraca wektor pomnożony przez podaną macierz"""
		#product = tuple(Vector( *row ) * vector for row in matrix)
		#return Vector( *product )
		x, y = vector.xy
		return cls( matrix.matrix[0][0] * x + matrix.matrix[0][1] * y, matrix.matrix[1][0] * x + matrix.matrix[1][1] * y )
		
	def tangent( self ):
		"""Zwraca wektor prostopadły"""
		x, y = self.xy
		return Vector( y, x )
	
	def norm( self ):
		"""Zwraca długość wektora"""
		return sqrt( sum( a**2 for a in self ) )
	
	def normalize( self ):
		"""Zwraca znormalizowany wektor, czyli o długości 1 i zachowanym kierunku"""
		normalized = tuple( a / self.norm() for a in self )
		return Vector( *normalized )
		 	
	def __add__( self, vec ):
		added = tuple(a + b for a, b in zip( self, vec ) )
		return Vector( *added ) 
	
	def __sub__( self, vec ):
		subbed = tuple(a - b for a, b in zip( self, vec ) )
		return Vector( *subbed ) 
		
	def __mul__( self, other ):
		"""Jeśli other to wektor to jest to iloczyn skalarny. W przeciwnym wypdku jest to mnożenie przez skalar"""
		if type( other ) == type( self ):
			return( sum( a * b for a, b in zip( self, other ) ) )
		if type( other ) == type( 1 ) or type( other ) == type( 1.0 ):
			mult = tuple( a * other for a in self )
			return Vector( *mult )
		
	def __div__( self, scalar ):
		return Vector( a / scalar for a in self )
	
	def __iter__(self):
		return self.xy.__iter__()
