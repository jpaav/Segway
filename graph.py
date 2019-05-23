import matplotlib

import matplotlib.backends.backend_agg as agg
import pygame as pg

import pylab


class Graph(pg.sprite.Sprite):

	def __init__(self):
		super().__init__()
		matplotlib.use("Agg")
		self.fig = pylab.figure(figsize=[8, 4], dpi=100)
		self.data = []
		self.data2 = []
		self.ax = self.fig.gca()
		# self.ax.plot(self.data)

		self.canvas = agg.FigureCanvasAgg(self.fig)
		self.canvas.draw()
		self.renderer = self.canvas.get_renderer()
		self.raw_data = self.renderer.tostring_rgb()

	def add_data_point(self, point):
		if self.data.__len__() > 20:
			self.data.pop(0)
		self.data.append(point)

	def add_data_point2(self, point):
		if self.data2.__len__() > 20:
			self.data2.pop(0)
		self.data2.append(point)

	def update_graph(self):
		pass
		# self.ax = self.fig.gca(autoscaley_on=False, ylim=(-5,5))
		self.ax.clear()
		self.ax.set_ylim(-95, 95)
		self.ax.plot(self.data, label='Angle')
		self.ax.plot(self.data2, label='PID output')
		self.ax.legend()

		# self.canvas = agg.FigureCanvasAgg(self.fig)
		self.canvas.draw()
		self.renderer = self.canvas.get_renderer()
		self.raw_data = self.renderer.tostring_rgb()

	def draw(self, screen):
		size = self.canvas.get_width_height()
		surf = pg.image.fromstring(self.raw_data, size, "RGB")
		screen.blit(surf, (0, 400))
