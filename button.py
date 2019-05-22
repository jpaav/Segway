import pygame as pg


class Button(pg.sprite.Sprite):
	def __init__(self, callback, text, x=0, y=0, w=100, h=30, color=None):
		super().__init__()
		self.callback = callback
		self.text = text
		self.rect = pg.Rect(x, y, w, h)
		if color is None:
			color = [0, 100, 0]
		self.background_color = color
		self.surface = pg.Surface((self.rect.w, self.rect.h))
		self.surface.fill(self.background_color)
		self.font = pg.font.SysFont('freesansbold.ttf', 24)
		self.screen = pg.display.get_surface()

	def draw(self):
		self.screen.blit(self.surface, self.rect)
		self.screen.blit(self.font.render(self.text, True, [255, 255, 255]), (self.rect.centerx-20, self.rect.centery-6))

	def click_at(self, pos):
		if self.rect.collidepoint(pos[0], pos[1]):
			self.callback()

