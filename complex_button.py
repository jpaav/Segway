import pygame as pg


class ComplexButton(pg.sprite.Sprite):
	def __init__(self, x=0, y=0, w=100, h=30, enabled=True, value=0.0, value_velocity=0.1, label="Label"):
		super().__init__()

		# Setup
		self.screen = pg.display.get_surface()

		# Rects
		self.full_rect = pg.Rect(x, y, w, h)
		self.left_rect = pg.Rect(x, y, int(w/3), h)
		self.center_rect = pg.Rect(x+int(w/3), y, int(w/3), h)
		self.right_rect = pg.Rect(x+2*int(w/3), y, int(w/3), h)

		# Values
		self.boolean = enabled
		self.value = value
		self.value_velocity = value_velocity

		# Aesthetics
		self.OFF_COLOR = [200, 0, 0]
		self.ON_COLOR = [0, 100, 0]
		self.surf = pg.Surface((self.full_rect.w, self.full_rect.h))
		if self.boolean:
			self.surf.fill(self.ON_COLOR)
		else:
			self.surf.fill(self.OFF_COLOR)
		# pg.font.init()
		self.font = pg.font.SysFont('freesansbold.ttf', 16)
		self.label = label

	def draw(self, screen):
		screen.blit(self.surf, self.full_rect)
		screen.blit(self.font.render("<", True, [255, 255, 255]), (self.left_rect.centerx-2, self.left_rect.centery-5))
		screen.blit(self.font.render(">", True, [255, 255, 255]), (self.right_rect.centerx-2, self.right_rect.centery-5))
		screen.blit(self.font.render(self.label, True, [255, 255, 255]), (self.left_rect.left, self.left_rect.top-10))
		screen.blit(self.font.render("{:.1f}".format(self.value), True, [255, 255, 255]), (self.center_rect.centerx-3, self.center_rect.centery-5))


	def click_at(self, pos):
		if not self.full_rect.collidepoint(pos[0], pos[1]):
			return False  # return early if the click wasn't in any of the rects
		if self.left_rect.collidepoint(pos[0], pos[1]):
			self.decrement_value()
			return True
		if self.right_rect.collidepoint(pos[0], pos[1]):
			self.increment_value()
			return True
		if self.center_rect.collidepoint(pos[0], pos[1]):
			self.toggle_boolean()
			return True

	def toggle_boolean(self):
		self.boolean = not self.boolean
		if self.boolean:
			self.surf.fill(self.ON_COLOR)
		else:
			self.surf.fill(self.OFF_COLOR)

	def increment_value(self):
		self.value += self.value_velocity

	def decrement_value(self):
		self.value -= self.value_velocity

