if __name__ == "__main__":

	from QuadTree import *
	
	pygame.init()
	
	#screen settings
	screen = pygame.display.set_mode( ( int(WINDOW_X * 2), int(WINDOW_Y * 2) ) )

	done = False
	
	number_of_particles = 300
	
	#create list of particle
	my_particles = []
	my_particles.extend(addParticles(screen, number_of_particles, (255, 0 , 0)))
	my_particles.extend(addParticles(screen, number_of_particles, (0, 255 , 0)))
	my_particles.extend(addParticles(screen, number_of_particles, (0, 0 , 255)))
	
	#create quad tree
	quadtree = QuadTree( 0, Border( -WINDOW_X, -WINDOW_Y, WINDOW_X * 2, WINDOW_Y * 2 ) )

	#starting clock
	clock = pygame.time.Clock()
	
	#set time of first frame
	deltatime = 0.02

	while not done:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		#add all of particle to quad tree
		for element in my_particles:
			quadtree.insert( element )
		
		#find collision
		quadtree.DFS()
		
		#update and draw particles
		for element in my_particles:
			element.update(deltatime)
			element.draw()
		
		#clear quad tree
		quadtree.clearTree()

		pygame.display.update()
		
		#time of frame
		#deltatime = clock.tick() * 0.001
		
		#clear screen
		screen.fill((0, 0, 0))
