import pygame as pg

from button import Button
from complex_button import ComplexButton
from segway import Segway
from graph import Graph


class Game:
	def __init__(self):
		self.width = 800
		self.height = 800
		self.should_quit = False

		# Init PyGame
		(passed, failed) = pg.init()
		print("Number of modules successfully loaded: " + str(passed))
		print("Number of modules failed to load: " + str(failed))

		# Create screen with given dimensions
		self.screen = pg.display.set_mode((self.width, self.height))
		pg.display.set_caption("Segway")
		pg.display.set_icon(pg.image.load("resources/beck_icon.png"))

		# Objects
		self.segway = Segway()
		self.graph = Graph()
		self.kp_button = ComplexButton(x=50, y=400, label="Kp", value_velocity=1)
		self.ki_button = ComplexButton(x=250, y=400, label="Ki")
		self.kd_button = ComplexButton(x=450, y=400, label="Kd")
		self.reset_button = Button(self.reset, "Reset", x=650, y=400)

	# This is a callback function passed to the reset button
	# This code is jank, fixing it may have performance increases on reset
	def reset(self):
		self.segway = Segway()
		self.graph = Graph()
		self.kp_button = ComplexButton(x=50, y=400, label="Kp", value_velocity=1)
		self.ki_button = ComplexButton(x=250, y=400, label="Ki")
		self.kd_button = ComplexButton(x=450, y=400, label="Kd")

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
		self.graph.add_data_point2(self.segway.pid.last_output)
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
			if event.type == pg.MOUSEBUTTONDOWN:
				pos = pg.mouse.get_pos()
				self.reset_button.click_at(pos)
				if self.kp_button.click_at(pos):
					self.segway.pid.p_enabled = self.kp_button.boolean
					self.segway.pid.Kp = self.kp_button.value
				if self.ki_button.click_at(pos):
					self.segway.pid.i_enabled = self.ki_button.boolean
					self.segway.pid.Ki = self.ki_button.value
				if self.kd_button.click_at(pos):
					self.segway.pid.d_enabled = self.kd_button.boolean
					self.segway.pid.Kd = self.kd_button.value

	def draw(self):
		self.screen.fill([0, 200, 0])
		self.segway.draw(self.screen)
		self.graph.draw(self.screen)
		self.kp_button.draw(self.screen)
		self.ki_button.draw(self.screen)
		self.kd_button.draw(self.screen)
		self.reset_button.draw()
