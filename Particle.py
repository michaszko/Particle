from Vector import *
from math import pi
from random import *
import pygame

#wymiary okna
WINDOW_X = 1280; WINDOW_Y = 720

def if_collide( ball1, ball2 ):
	"""Sprawdza czy podane kulki ze sobą kolidują. Jeśli tak zwraca True"""
	
	b1_x, b1_y = ball1.position.xy
	b2_x, b2_y = ball2.position.xy
	
	#wektror łączący środki kół
	distant = Vector.from_points((b2_x, b2_y), (b1_x, b1_y))
	
	#jeśli długość powyższego wektora jest mniejsza(równa) niż suma promieni ( czyli na siebie nachodzą )
	if ball1.r + ball2.r >= distant.norm():
		return True
	else:
		return False
		
def collide( ball1, ball2 ):
	"""Zmienia parametrów zderzonych kulek"""
		
	#wzory z wikipedi na zmianę prędkości
	a = 2 * float(ball2.mass / (ball1.mass + ball2.mass))								# 2 * m2 / ( m1 + m2 )  
	b = (ball1.velocity - ball2.velocity) * (ball1.position - ball2.position)			# < v1 - v2, x1 - x2 >
	c = (ball1.position - ball2.position).norm() ** 2									# || x1 - x2 || ^ 2
	d = a * b / c
	b1_velocity = ball1.velocity - (ball1.position - ball2.position) * d
	
	a = 2 * float(ball1.mass / (ball1.mass + ball2.mass))								# 2 * m1 / ( m1 + m2 )  
	b = (ball2.velocity - ball1.velocity) * (ball2.position - ball1.position)			# < v2 - v1, x2 - x1 >
	c = (ball2.position - ball1.position).norm() ** 2									# || x2 - x1 || ^ 2
	d = a * b / c
	b2_velocity = ball2.velocity - (ball2.position - ball1.position) * d
	
	#wpisanie nowych prędkości
	ball1.velocity = b1_velocity
	ball2.velocity = b2_velocity

	#zmiana koloru - obie będą miały uśredniony koloru
	ball1.color = ball2.color = ( (ball1.color[0] + ball2.color[0]) * 0.5, (ball1.color[1] + ball2.color[1]) * 0.5, (ball1.color[2] + ball2.color[2]) * 0.5)

def add_particles( screen, number, color ):
	"""Tworzy listę losowych particli i ją zwraca"""
	
	particles = []
	
	for i in range( number ):
		particles.append( Ball( screen, randint(-WINDOW_X * 0.5 + 10, 1), randint(-WINDOW_Y * 0.5 + 10, 1), randrange(-1, 2, 2) * 100, randrange(-1, 2, 2) * 100, 10, 1, color ))
	
	return particles
		
class Ball( object ):

	def __init__( self, screen, x=0.0, y=0.0, vx=0.0, vy=0.0, r=1.0, m=1.0, color=(255,255,0) ):
		"""
			Towrzy kukę w pozycji (x, y), o prędkości (vx, vy), masie 'm' i promieniu 'r'.
			Kolor jest nadawany w zależności od położenia.
			Początek układu współrzędnych jest w punkcie (WINDOW_X / 2 , WINDOW_Y / 2)
		"""
		self.position = Vector( x, y )
		self.velocity = Vector( vx, vy )
		self.mass = m
		self.r = int(r)
		self.color = color
		#self.color = ( int((abs(x) / WINDOW_X) * 255 * 2), 0, int((abs(y) / WINDOW_Y) * 255 * 2))
		self.screen = screen
	
	def __str__( self ):
		"""Konwersja kulki do stringa"""
		x, y = self.position.xy
		vx, vy = self.velocity.xy
		return 'This ball position is ( {0} , {1} ), velocity ( {2} , {3} ) and radius {4}'.format(x, y, vx, vy, self.r) 
	
	def check_edges( self ):
		"""Sprawdza czy kulka zderza się ze ścianką. Jeśli tak to się odbija."""
		x, y = self.position.xy
		vx, vy = self.velocity.xy
		
		def sign( a ):
			if a > 0:
				return 1
			elif a == 0:
				return 0
			elif a < 0:
				return -1
		
		if abs( x ) > WINDOW_X * 0.5 - self.r:
			k = sign( vx )
			vx *= -1
			x = k * (WINDOW_X * 0.5 - self.r)
			
		
		if abs( y ) > WINDOW_Y * 0.5 - self.r:
			k = sign( vy )
			vy *= -1
			y = k * (WINDOW_Y * 0.5 - self.r)
			
		self.position.xy = (x, y)
		self.velocity.xy = (vx, vy)
	
	def change_color( self ):
		"""Zmienia kolor w zależności od pozycji"""
		x, y = self.position.xy
		self.color = ( int((x / WINDOW_X) * 128), int((x / WINDOW_X) * 128) + int((y / WINDOW_Y) * 128 ), int((y / WINDOW_Y) * 128))
			
	def move( self, deltatime ):
		"""Porusza kulkę"""
		self.position += self.velocity * deltatime
	
	def update( self, deltatime ):
		self.check_edges()
		#self.change_color()
		self.move( deltatime )
		
	def draw( self ):
		"""Musiimy przekonwertować położenie każdego punktu do współrzędnych o środku w lewym górnym rogu"""
			
		transposition = lambda point: (point[0] + WINDOW_X * 0.5, WINDOW_Y * 0.5 - point[1])
			 
		x, y = transposition( self.position.xy )
		pygame.draw.circle(self.screen, self.color, ( int(x + 0.5), int(y + 0.5) ), self.r)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
