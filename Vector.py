from math import sqrt, acos

def dot_product( v1, v2 ):
	return( v1.x * v2.x + v1.y * v2.y )

def angle( v1, v2 ):
	return(acos( dot_product( v1, v2 ) / ( v1.norm() * v2.norm() ) ))
	
def cosinus( v1, v2 ):
	return( dot_product( v1, v2 ) / ( v1.norm() * v2.norm() ) )
	
class Vector( object ):
	
	def __init__( self, x=0.0, y=0.0 ):
		self.x = x
		self.y = y
		
	def __str__( self ):
		return '({0} , {1})'.format(self.x, self.y)
	
	@classmethod	
	def from_points( cls, P1, P2 ):
		return cls( P2[0] - P1[0], P2[1] - P1[1] )
	
	@classmethod
	def matrix_mul( cls, matrix, vector):
		return cls( matrix.matrix[0][0] * vector.x + matrix.matrix[0][1] * vector.y, matrix.matrix[1][0] * vector.x + matrix.matrix[1][1] * vector.y )
		
	def tangent( self ):
			return Vector( self.y, -self.x )
	
	def norm( self ):
		return sqrt( self.x**2 + self.y**2 )
		
	def __add__( self, vec ):
		return Vector( self.x + vec.x, self.y + vec.y )
	
	def __sub__( self, vec ):
		return Vector( self.x - vec.x, self.y - vec.y )
		
	def __mul__( self, scalar ):
		return Vector( self.x * scalar, self.y * scalar )
		
	def __div__( self, scalar ):
		return Vector( self.x / scalar, self.y / scalar )
