if __name__ == "__main__":

	from Particle import *

	pygame.init()
	
	screen = pygame.display.set_mode( ( WINDOW_X, WINDOW_Y ) )

	done = False
	
	#tworzymy liste particli
	my_particles = []
	my_particles.extend(add_particles(screen, 30, (255, 0 , 0)))
	my_particles.extend(add_particles(screen, 30, (0, 255 , 0)))
	my_particles.extend(add_particles(screen, 30, (0, 0 , 255)))
	
	#tworzymy listę koldujących ze sobą particli
	collided = []

	#startujemy zegarek
	clock = pygame.time.Clock()
	
	#ustawaimy czas pierwszej klatki
	deltatime = 0.1

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		
		#czyścimy ekran
		screen.fill((0, 0, 0))
		
		#sprawdzamy dla każdych dwóch particli czy się nie zderzyły
		for i, particle in enumerate(my_particles):
		
			for particle2 in my_particles[i+1:]:
			
				if (particle, particle2) not in collided and if_collide(particle, particle2) == True:		#jeśli się zderzyły nie nie zderzyły się w poprzedniej klatce to
					collide(particle, particle2)															#zmień ich prędkość
					collided.append((particle, particle2))													#i dodaj do listy ostatnio odbitych
					
				elif (particle, particle2) in collided and if_collide(particle, particle2) == False:		#jeśli się nie zdrzyły ale zderzyłys się w porzedniej klatce to
					collided.remove((particle, particle2))													#usuń z listy ostatnio odbitych
					
			#jeśli particle są na liście i zderzyły się do nie nastapi odbicie - będą dla siebie transparentne

			particle.update(deltatime)
			particle.draw()
		
		#print(my_particles[0])

		pygame.display.update()
		
		#stąd bierzemy czas jaki upłynął od ostatniej klatki ( w sekundach )
		deltatime = clock.tick(60) * 0.001
