from Vector import *
from random import randint, randrange
import pygame

#window resolution
WINDOW_X = 1280 / 2; WINDOW_Y = 720 / 2

def ifCollide( ball1, ball2 ):
	"""
		Check if particles collide witch each other
		If so - True is returned. Otherwise False
	"""
	
	b1_x, b1_y = ball1.position.xy
	b2_x, b2_y = ball2.position.xy
	
	#vector connect center of particles
	distant = Vector.from_points((b2_x, b2_y), (b1_x, b1_y))
	
	#if lenght of vector above is less( equal ) than  sum of radius ( they overlapping )
	if ( ball1.r + ball2.r ) ** 2 >= distant.norm():
		return True
	else:
		return False


def collision( ball1, ball2 ):
	"""
		Changing parameters of particles
	"""
		
	#equation from wikipedia
	a1 = 2 * float(ball2.mass / (ball1.mass + ball2.mass))								# 2 * m2 / ( m1 + m2 )  
	a2 = 2 - a1																			# 2 * m1 / ( m1 + m2 ) = 2 - m2 / ( m1 + m2 )  
	b = (ball1.velocity - ball2.velocity) * (ball1.position - ball2.position)			# < v1 - v2, x1 - x2 > = < v2 - v1, x2 - x1 >
	c = (ball1.position - ball2.position).norm() 										# || x1 - x2 || ^ 2	= || x2 - x1 || ^ 2	
	if c == 0:
		c = 0.01						
	d = b / c

	#enter new velocites
	ball1.velocity = ball1.velocity - (ball1.position - ball2.position) * a1 * d
	ball2.velocity = ball2.velocity - (ball2.position - ball1.position) * a2 * d

	#changing color 
	ball1.color = ball2.color = ( 	(ball1.color[0] + ball2.color[0]) * 0.5, 
									(ball1.color[1] + ball2.color[1]) * 0.5, 
									(ball1.color[2] + ball2.color[2]) * 0.5		)


def addParticles( screen, number, color ):
	"""
		Create a list of random particles and return it
	"""
	
	particles = []
	
	for i in range( number ):
	
		radius = 5
		mass = 1
		
		#random position and velocity
		x, y = randint(-WINDOW_X + radius, 1), randint(-WINDOW_Y + radius, WINDOW_Y - radius)
		vx, vy = randrange(-1, 2, 2) * 100, randrange(-1, 2, 2) * 100
		
		particles.append( Particle( screen, x, y, vx, vy, radius, mass, color ))
	
	return particles
	
######################################################################################################
		
class Particle( object ):
	"""
		Class of particle with position, velocity, mass and color represented by circle
	"""

	def __init__( self, screen, x=0.0, y=0.0, vx=0.0, vy=0.0, r=1.0, m=1.0, color=(255,255,0) ):
		"""
			Create particle in position (x, y) with velocity (vx, vy), mass, radius, color
			Point (0, 0) is in the middle of screen which is pont (WINDOW_X / 2 , WINDOW_Y / 2) in normal coordinate
		"""
		
		self.position = Vector( x, y )
		self.velocity = Vector( vx, vy )
		self.mass = m
		self.r = int(r)
		self.color = color
		self.screen = screen
	
	
	def __str__( self ):
		"""
			Convert particle to string
		"""
		
		x, y = self.position.xy
		vx, vy = self.velocity.xy
		
		return 'This ball position is ( {0} , {1} ), velocity ( {2} , {3} ) and radius {4}'.format(x, y, vx, vy, self.r) 
	
	
	def checkEdges( self ):
		"""
			Check if particle collide with wall
			If so - change velocity
		"""
		x, y = self.position.xy
		vx, vy = self.velocity.xy
		
		#if particle hit left or right wall
		if abs( x ) > WINDOW_X - self.r:
			#change vertical speed
			vx *= -1
			
		#if particle hit top or bottom wall
		if abs( y ) > WINDOW_Y - self.r:
			#change horizontal speed
			vy *= -1
		
		#enter new velocity
		self.velocity.xy = (vx, vy)
	
	
	def changeColor( self ):
		"""
			Changing color of particle
		"""
		
		x, y = self.position.xy
		self.color = ( int((x / WINDOW_X) * 128), int((x / WINDOW_X) * 128) + int((y / WINDOW_Y) * 128 ), int((y / WINDOW_Y) * 128))
		
			
	def move( self, deltatime ):
		"""
			Move particle
		"""
		
		#just adding velocity to current position
		self.position += self.velocity * deltatime
	
	
	def update( self, deltatime ):
		"""
			Check and move
		"""
		
		self.checkEdges()
		#self.changeColor()
		self.move( deltatime )
		
		
	def draw( self ):
		"""
			Draw particle in converted coordinate
		"""
			
		transposition = lambda point: (point[0] + WINDOW_X, WINDOW_Y - point[1])
			 
		x, y = transposition( self.position.xy )
		pygame.draw.circle(self.screen, self.color, ( int(x + 0.5), int(y + 0.5) ), self.r)
		
##########################################################################################################
