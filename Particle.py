from Vector import *
from Rotation_matrix import *
from math import pi
import pygame

WINDOW_X = 1280; WINDOW_Y = 720

def collide( ball1, ball2 ):
	b1_x, b1_y = ball1.position.xy
	b2_x, b2_y = ball2.position.xy
	
	b1_vx, b1_vy = ball1.velocity.xy
	b2_vx, b2_vy = ball2.velocity.xy
	
	#wektror łączący środki kół
	distant = Vector.from_points((b2_x, b2_y), (b1_x, b1_y))
	
	#jeśli długość powyższego wektora jest mniejsza(równa) niż suma promieni ( czyli na siebie nachodzą )
	if ball1.r + ball2.r >= distant.norm():
	
		#wzory z wikipedi
		a = 2 * float(ball2.mass / (ball1.mass + ball2.mass))
		b = (ball1.velocity - ball2.velocity) * (ball1.position - ball2.position)
		c = (ball1.position - ball2.position).norm() ** 2
		d = a * b / c
		b1_velocity = ball1.velocity - (ball1.position - ball2.position) * d
		
		a = 2 * float(ball1.mass / (ball1.mass + ball2.mass))
		b = (ball2.velocity - ball1.velocity) * (ball2.position - ball1.position)
		c = (ball2.position - ball1.position).norm() ** 2
		d = a * b / c
		b2_velocity = ball2.velocity - (ball2.position - ball1.position) * d
		
		ball1.velocity = b1_velocity
		ball2.velocity = b2_velocity
		
		ball1.position += ball1.velocity 
		ball2.position += ball2.velocity 
		
class Ball( object ):

	def __init__( self, screen, x=0.0, y=0.0, vx=0.0, vy=0.0, r=1.0, m=1.0 ):
		self.position = Vector( x, y )
		self.velocity = Vector( vx, vy )
		self.mass = m
		self.r = int(r)
		self.color = ( int((x / WINDOW_X) * 128) + int((y / WINDOW_Y) * 128), 0, 0 )
		self.screen = screen
	
	def __str__( self ):
		x, y = self.position.xy
		vx, vy = self.velocity.xy
		return 'This ball position is ( {0} , {1} ), velocity ( {2} , {3} ) and radius {4}'.format(x, y, vx, vy, self.r) 
	
	def check_edges( self ):
		x, y = self.position.xy
		vx, vy = self.velocity.xy
		
		if x > WINDOW_X - self.r:
			vx *= -1
			x = WINDOW_X - self.r
		elif x < self.r:
			vx *= -1
			x = self.r
		
		if y > WINDOW_Y - self.r:
			vy *= -1
			y = WINDOW_Y - self.r
		elif y < self.r:
			vy *= -1
			y = self.r
			
		self.position.xy = (x, y)
		self.velocity.xy = (vx, vy)
	
	def change_color( self ):
		x, y = self.position.xy
		self.color = ( int((x / WINDOW_X) * 128), int((y / WINDOW_Y) * 128), int((x / WINDOW_X) * 128) + int((y / WINDOW_Y) * 128 ))
			
	def move( self ):
		self.position += self.velocity
	
	def update( self ):
		self.check_edges()
		self.change_color()
		self.move()
		
	def draw( self ):
		x, y = self.position.xy
		pygame.draw.circle(self.screen, self.color, ( int(x), int(y) ), self.r)
