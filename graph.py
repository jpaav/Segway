import matplotlib
matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg
import pygame as pg

import pylab
import thorpy


class Graph(pg.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.fig = pylab.figure(figsize=[8, 4], dpi=100)
		self.data = []
		self.ax = self.fig.gca()
		self.ax.plot(self.data)

		self.canvas = agg.FigureCanvasAgg(self.fig)
		self.canvas.draw()
		self.renderer = self.canvas.get_renderer()
		self.raw_data = self.renderer.tostring_rgb()
		# self.kp_slider = thorpy.SliderX(length=100, limvals=(-5, 5), text="Kp", initial_value=1, type_=float)
		# self.ki_slider = thorpy.SliderX(length=100, limvals=(-5, 5), text="Ki", initial_value=1, type_=float)
		# self.kd_slider = thorpy.SliderX(length=100, limvals=(-5, 5), text="Kd", initial_value=1, type_=float)

	def add_data_point(self, point):
		# if self.data.__len__() > 20:
		# 	self.data.pop(0)
		self.data.append(point)

	def update_graph(self):
		self.ax = self.fig.gca()
		self.ax.plot(self.data)


		# self.canvas = agg.FigureCanvasAgg(self.fig)
		self.canvas.draw()
		self.renderer = self.canvas.get_renderer()
		self.raw_data = self.renderer.tostring_rgb()

	def draw(self, screen):
		size = self.canvas.get_width_height()
		surf = pg.image.fromstring(self.raw_data, size, "RGB")
		screen.blit(surf, (0,400))
