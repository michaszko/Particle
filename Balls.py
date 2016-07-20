from Vector import *
from Rotation_matrix import *
from math import pi
import pygame

def collide( ball1, ball2 ):
	distant = Vector.from_points((ball2.position.x, ball2.position.y), (ball1.position.x, ball1.position.y))
	if ball1.r + ball2.r >= distant.norm():
		tangent = distant.tangent()
		alpha = angle( tangent, ball1.velocity )
		if alpha >= pi:
			alpha -= pi
		ball1.position -= ball1.velocity
		ball1.velocity = Vector.matrix_mul( Matrix( 2*alpha ), ball1.velocity ) * -1
		ball1.position += ball1.velocity
		
	
		distant *= -1
		tangent = distant.tangent()
		alpha = angle( tangent, ball1.velocity )
		if alpha >= pi/2:
			alpha -= pi/2
		ball2.position -= ball2.velocity
		ball2.velocity = Vector.matrix_mul( Matrix( 2*alpha ), ball2.velocity ) 
		ball2.position += ball2.velocity
		
class Ball( object ):

	def __init__( self, screen, x=0.0, y=0.0, vx=0.0, vy=0.0, r=1.0 ):
		self.position = Vector( x, y )
		self.velocity = Vector( vx, vy )
		self.color = ( int((x / 640.0) * 128) + int((y / 640.0) * 128), 0, 0 )
		self.r = int(r)
		self.screen = screen
	
	def __str__( self ):
		return 'This ball position is ( {0} , {1} ), velocity ( {2} , {3} ) and radius {4}'.format(self.position.x, self.position.y, self.velocity.x, self.velocity.y, self.r) 
	
	def check_edges( self ):
		if self.position.x > 640 - self.r:
			self.velocity.x *= -1
			self.position.x = 640 - self.r
		elif self.position.x < self.r:
			self.velocity.x *= -1
			self.position.x = self.r
		
		if self.position.y > 480 - self.r:
			self.velocity.y *= -1
			self.position.y = 480 - self.r
		elif self.position.y < self.r:
			self.velocity.y *= -1
			self.position.y = self.r
	
	def change_color( self ):
		self.color = ( int((self.position.x / 640.0) * 128), int((self.position.y / 480.0) * 128), int((self.position.x / 640.0) * 128) + int((self.position.y / 480.0) * 128 ))
			
	def move( self ):
		self.position += self.velocity
	
	def update( self ):
		self.check_edges()
		self.change_color()
		self.move()
		
	def draw( self ):
		pygame.draw.circle(self.screen, self.color, ( int(self.position.x), int(self.position.y) ), self.r)
		
