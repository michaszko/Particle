from math import acos


def angle( v1, v2 ):
	"""
		Return angle between two vectors
	"""
	
	return(acos( v1 * v2 / ( v1.norm() * v2.norm() ) ))
	
	
def cosinus( v1, v2 ):
	"""
		Return cosinus of angle between two vectors
	"""
	
	return( v1 * v2 / ( v1.norm() * v2.norm() ) )
	
###########################################################################################
	
class Vector( object ):
	"""
		Class of 2 - dimentional vectors
	"""
	
	
	def __init__( self, *args ):
		"""
			Create vector with values (x, y)
		"""            
		
		self.xy = args
		
		
	def __repr__( self ):
		"""
			Convert to string
		"""
		
		return "({0} , {1})".format(self.xy[0], self.xy[1])
	
	
	@classmethod	
	def from_points( cls, P1, P2 ):
		"""
			Return vector that connect two points
		"""
		
		return cls( P2[0] - P1[0], P2[1] - P1[1] )
	
	
	@classmethod
	def matrix_mult( cls, matrix, vector):
		"""
			Return vector multiplied by matrix
		"""
		
		x, y = vector.xy
		return cls( matrix.matrix[0][0] * x + matrix.matrix[0][1] * y, matrix.matrix[1][0] * x + matrix.matrix[1][1] * y )
		
		
	def tangent( self ):
		"""
			Return tangent vector
		"""
		
		x, y = self.xy
		return Vector( y, -x )
	
	
	def norm( self ):
		"""
			Return squere of vector lenght 
		"""
		
		return sum( a**2 for a in self )
	
	
	def normalize( self ):
		"""
			Return normalized vector
		"""
		
		normalized = tuple( a / self.norm() for a in self )
		return Vector( *normalized )
		
		 	
	def __add__( self, vec ):
		"""
			Return sum of two vectors
		"""
		
		added = tuple(a + b for a, b in zip( self, vec ) )
		return Vector( *added ) 
	
	
	def __sub__( self, vec ):
		"""
			Return diff of two vectors
		"""
		
		subbed = tuple(a - b for a, b in zip( self, vec ) )
		return Vector( *subbed ) 
		
		
	def __mul__( self, other ):
		"""
			If other is a vector then it is dot product
			If it scalar then it is normal product
		"""
		
		if type( other ) == type( self ):
			return( sum( a * b for a, b in zip( self, other ) ) )
			
		if type( other ) == type( 1 ) or type( other ) == type( 1.0 ):
			mult = tuple( a * other for a in self )
			return Vector( *mult )
		
		
	def __div__( self, scalar ):
		"""
			Return vector divided by scalar
		"""
		
		divided = tuple(a / scalar for a in self )
		return Vector( *divided )
	
	
	def __iter__(self):
		"""
			Convert to iterable
		"""
		
		return self.xy.__iter__()
		
###############################################################################################
