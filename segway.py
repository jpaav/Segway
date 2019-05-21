import pygame as pg
import numpy as np


class Segway:
	def __init__(self, width=200, height=200):
		self.width = width
		self.height = height
		self.image = pg.image.load('resources/segway.png')
		self.image = pg.transform.scale(self.image, (self.width, self.height))
		self.position = np.array([0, 0])
		self.moveright = False
		self.moveleft = False
		self.angle = 0
		self.image_rect = self.image.get_rect()

	def draw(self, screen):
		screen.blit(self.image, self.image_rect)

	def move_right(self):
		self.moveright = True

	def move_left(self):
		self.moveleft = True

	def stop_moving_right(self):
		self.moveright = False

	def stop_moving_left(self):
		self.moveleft = False

	def update_position(self):
		if self.moveright:
			self.position[0] += 10
			self.image = self.rotate(5)

		if self.moveleft:
			self.position[0] -= 10
			self.image = self.rotate(-5)

	def rotate(self, angle):
		image_orig = self.image
		self.image_rect = image_orig.get_rect(center=self.image_rect.center)
		# process
		image = pg.transform.rotate(image_orig, angle)
		self.image_rect = image.get_rect(center=self.image_rect.center)
		self.image = image

