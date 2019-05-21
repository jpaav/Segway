import pygame as pg
from segway import Segway
from graph import Graph

class Game:
	def __init__(self):
		self.width = 800
		self.height = 800
		self.should_quit = False
		self.segway = Segway()
		self.graph = Graph()

		# Init PyGame
		(passed, failed) = pg.init()
		print("Number of modules successfully loaded: " + str(passed))
		print("Number of modules failed to load: " + str(failed))

		# Create screen with given dimensions
		self.screen = pg.display.set_mode((self.width, self.height))
		pg.display.set_caption("Segway")

	def start(self):
		# Loop until should_quit is changed to true
		while not self.should_quit:
			self.loop()
		return 0

	def loop(self):
		self.check_events()
		self.segway.update_position()
		self.draw()
		self.graph.add_data_point(self.segway.angle)
		self.graph.update_graph()
		# pg.display.update()
		pg.display.flip()
		# clock.tick(30)

	def check_events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.should_quit = True
			# Check keypress
			if event.type == pg.KEYDOWN:
				# Quit on escape
				if event.key == pg.K_ESCAPE:
					self.should_quit = True
				if event.key == pg.K_LEFT:
					self.segway.move_left()
				if event.key == pg.K_RIGHT:
					self.segway.move_right()
			if event.type == pg.KEYUP:
				if event.key == pg.K_LEFT:
					self.segway.stop_moving_left()
				if event.key == pg.K_RIGHT:
					self.segway.stop_moving_right()

	def draw(self):
		self.screen.fill([0, 200, 0])
		self.segway.draw(self.screen)
		self.graph.draw(self.screen)
