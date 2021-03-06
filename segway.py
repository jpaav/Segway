import pygame as pg
from pygame.math import Vector2
from PID import PID
import math


class Segway(pg.sprite.Sprite):

	def __init__(self, width=250, height=250, speed=20):
		super().__init__()
		self.width = width
		self.height = height
		self.image = pg.image.load('resources/beck_segway_final.png')
		self.image = pg.transform.scale(self.image, (self.width, self.height))
		self.position = Vector2(250, 250)
		self.moveright = False
		self.moveleft = False
		self.speed = speed
		#PID
		self.pid = PID()
		# A reference to the original image to preserve the quality.
		self.orig_image = self.image.copy()
		self.rect = self.image.get_rect(center=self.position)
		self.offset = Vector2(0, -50)  # We shift the sprite 50 px to the right.
		self.angle = 0
		self.angle_vel = 0

	def draw(self, screen):
		screen.blit(self.image, self.rect)

	def move_right(self):
		self.moveright = True

	def move_left(self):
		self.moveleft = True

	def stop_moving_right(self):
		self.moveright = False

	def stop_moving_left(self):
		self.moveleft = False

	def update_position(self):
		accel = 2
		self.angle_vel += math.sin((self.angle / 180) * math.pi) * accel
		self.angle += self.angle_vel + self.pid.pid(self.angle, 0)

		if self.moveright:
			self.position[0] += self.speed
			self.angle += 10

		if self.moveleft:
			self.position[0] -= self.speed
			self.angle -= 10

		self.rotate()

		if self.angle > 90:
			self.angle = 90
			self.angle_vel = 0
		elif self.angle < -90:
			self.angle = -90
			self.angle_vel = 0

	def rotate(self):
		"""Rotate the image of the sprite around a pivot point."""
		# Rotate the image.
		self.image = pg.transform.rotozoom(self.orig_image, -self.angle, 1)
		# Rotate the offset vector.
		offset_rotated = self.offset.rotate(self.angle)
		# Create a new rect with the center of the sprite + the offset.
		self.rect = self.image.get_rect(center=self.position + offset_rotated)

	def reset(self):
		self.angle_vel = 0
		self.angle = 0
		self.position = Vector2(250, 250)
		self.pid.reset_history()


