import matplotlib
matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg
import pygame as pg

import pylab


class Graph(pg.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.fig = pylab.figure(figsize=[8, 4], dpi=100)
		self.ax = self.fig.gca()
		self.ax.plot([1, 2, 4])

		self.canvas = agg.FigureCanvasAgg(self.fig)
		self.canvas.draw()
		self.renderer = self.canvas.get_renderer()
		self.raw_data = self.renderer.tostring_rgb()

	def draw(self, screen):
		size = self.canvas.get_width_height()
		surf = pg.image.fromstring(self.raw_data, size, "RGB")
		screen.blit(surf, (0,400))
