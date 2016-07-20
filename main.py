if __name__ == "__main__":

	WINDOW_X = 640; WINDOW_Y = 480

	from random import *
	import pygame
	from Balls import *

	pygame.init()


	screen = pygame.display.set_mode( ( WINDOW_X, WINDOW_Y ) )

	done = False
	
	rotation = Matrix( 0.1 )
	
	my_particles = []
	for i in range(30):
		my_particles.append( Ball( screen, randint(0, 640), randint(0, 480), randint(1, 6) - 5, randint(1, 6) - 5, 10 ))

	clock = pygame.time.Clock()

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		
		screen.fill((0, 0, 0))
		
		for i, particle in enumerate(my_particles):
			for particle2 in my_particles[i+1:]:
				collide(particle, particle2)
			particle.update()
			particle.draw()
			
#		print(my_particles[1])
#		print(cosinus(my_particles[1].position, my_particles[2].position))
#		print( Vector.matrix_mul( rotation, my_particles[1].position ))
#		print(my_particles[1].position.tangent())
		pygame.display.update()
		clock.tick(30)
