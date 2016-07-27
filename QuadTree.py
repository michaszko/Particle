from Vector import *
from Particle import *

#######################################################################################

class Border( object ):
	"""
		Class of rectangle with left - top corner provided
		Used as border in QuadTree class
	"""
	
	
	def __init__( self, x, y, width, height ):
		"""
			Create border with left top corner in (x, y) and with width and height
		"""
		
		self.x, self.y = x, y
		self.width, self.height = width, height
		
		
	def containsBall( self, ball ):
		"""
			Check if particle intersects with rectangle
		"""
		
		x, y = ball.position.xy
		r = ball.r
		
		if not self.x < x + r:
			return False
			
		if not self.x + self.width > x - r:
			return False
			
		if not self.y + self.height > y - r:
			return False
			
		if not self.y < y + r:
			 return False
		
		return  True
					
			
	def intersects( self, other ):
		"""
			Check if one border intersects with another
		"""
		return ( not( self.center_x - self.width > other.center_x + other.width or
			self.center_x + self.width < other.center_x - other.width or
			self.center_y + self.height > other.center_y + other.height or 
			self.center_y - self.height < other.center_y - other.height ) )
			
########################################################################################

collided = []	
	
########################################################################################	

class QuadTree( object ):
	"""
		Class of quad tree with particle in it
	"""
	
	MAX_CAPACITY = 2
	MAX_LEVEL = 5

	def __init__( self, level, boundary ):
		"""
			Create quad tree with deep level and border which can contain particle 
		"""
		
		self.boundary = boundary
		
		self.level = level
		
		self.balls = []
		
		self.NorthWest = None
		self.NorthEast = None
		self.SouthWest = None
		self.SouthEast = None
		
				
	def clearTree( self ):
		"""
			Clear quad tree	recursively
		"""
		
		self.balls.clear()
		
		for element in [self.NorthWest, self.NorthEast, self.SouthWest, self.SouthEast]:
		
			 if element != None:
			 
			 	element.clearTree()
			 	element = None

	def insert( self, ball ):
		"""
			Add particle to that node which intersects with it
		"""
		
		if not self.boundary.containsBall( ball ):
			return False
		
		if self.NorthWest == None:
		
			self.balls.append( ball )
			
			if len( self.balls ) > QuadTree.MAX_CAPACITY and self.level < QuadTree.MAX_LEVEL:
				
				self.split()
				
				for element in self.balls:
		
					self.NorthWest.insert( element ) 
					self.NorthEast.insert( element ) 
					self.SouthEast.insert( element ) 
					self.SouthWest.insert( element )
					self.balls.remove( element )
				
				return True
		
		if self.NorthWest != None:
		
			self.NorthWest.insert( ball ) 
			self.NorthEast.insert( ball ) 
			self.SouthEast.insert( ball ) 
			self.SouthWest.insert( ball )
			
			return True
		
		return False
		
				
	def split( self ):
		"""
			Split up node into 4 smaller one and sort particle 
		"""
		
		x, y = self.boundary.x, self.boundary.y
		width, height = self.boundary.width * 0.5, self.boundary.height * 0.5
		
		self.NorthWest = QuadTree( self.level + 1, Border( x, y, width, height ) ) 
		self.NorthEast = QuadTree( self.level + 1, Border( x + width, y, width, height ) )   
		self.SouthWest = QuadTree( self.level + 1, Border( x, y + height, width, height ) )   
		self.SouthEast = QuadTree( self.level + 1, Border( x + width, y + height, width, height ) )  

			
	def queryRange( self, _range ):
		"""
			Return list of particles colliding with _range rectangle
		"""
	
		self.ballsInRange = []
		
		if not self.boundary.intersects( _range ):
			return self.ballsInRange
			
		for element in self.balls:
			if _range.containsBall( element ):
				ballsInRange.append( element )
		
		if self.NorthWest == None:
			return ballsInRange
		
		ballsInRange.append( self.NorthWest.queryRange( _range ) )
		ballsInRange.append( self.NorthEast.queryRange( _range ) )
		ballsInRange.append( self.SouthWest.queryRange( _range ) )
		ballsInRange.append( self.SouthEast.queryRange( _range ) )
		
	
	def DFS( self ):
		"""
			Searching tree recursively and detect collision
		"""
		
		if self.NorthWest != None:
		
			self.NorthWest.DFS()
			self.NorthEast.DFS()
			self.SouthWest.DFS()
			self.SouthEast.DFS()
		
		else:
			
			for i, particle in enumerate(self.balls):

				for particle2 in self.balls[i+1:]:
				
					on_list = (particle, particle2) in collided or (particle2, particle) in collided
					if_col = ifCollide(particle, particle2)

					if not on_list and if_col:		#if they collide with each other...
						collision(particle, particle2)															#...change their velocites...
						collided.append((particle, particle2))													#...and add them to list of recent collided
	
					elif on_list and not if_col:			#if they NOT collide but collided in last frame...
						collided.remove((particle, particle2))													#...remove from list of recent collided
	
				#if particles are on list and collide - they wouldn't affect themselves
		
########################################################################################	

