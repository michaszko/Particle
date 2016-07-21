if __name__ == "__main__":

	from random import *
	import pygame
	from Particle import *

	pygame.init()


	screen = pygame.display.set_mode( ( WINDOW_X, WINDOW_Y ) )

	done = False
	
	rotation = Matrix( 0.1 )
	
	my_particles = []
	for i in range(100):
		my_particles.append( Ball( screen, randint(0, WINDOW_X), randint(0, WINDOW_Y), randint(1, 6) - 5, randint(1, 6) - 5, 10, 10 ))

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
