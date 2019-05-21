import matplotlib
from matplotlib.widgets import Slider

import matplotlib.backends.backend_agg as agg
import pygame as pg

import pylab
# import thorpy
# from kivy.uix.slider import Slider


class Graph(pg.sprite.Sprite):

	def __init__(self):
		super().__init__()
		matplotlib.use("Agg")
		self.fig = pylab.figure(figsize=[8, 4], dpi=100)
		self.data = []
		self.ax = self.fig.gca()
		# self.ax.plot(self.data)

		self.canvas = agg.FigureCanvasAgg(self.fig)
		self.canvas.draw()
		self.renderer = self.canvas.get_renderer()
		self.raw_data = self.renderer.tostring_rgb()
		# self.kp_slider = thorpy.SliderX(length=100, limvals=(-5, 5), text="Kp", initial_value=1, type_=float)
		# self.ki_slider = thorpy.SliderX(length=100, limvals=(-5, 5), text="Ki", initial_value=1, type_=float)
		# self.kd_slider = thorpy.SliderX(length=100, limvals=(-5, 5), text="Kd", initial_value=1, type_=float)

		# self.s = Slider(min=-100, max=100, value=25)

		self.kp_slider = Slider(self.ax, 'Test', 0.1, 30.0, valinit=0, valstep=0.1)

	def add_data_point(self, point):
		if self.data.__len__() > 20:
			self.data.pop(0)
		self.data.append(point)

	def update_graph(self):
		pass
		# self.ax = self.fig.gca(autoscaley_on=False, ylim=(-5,5))
		self.ax.clear()
		self.ax.set_ylim(-15,15)
		self.ax.plot(self.data)

		# self.canvas = agg.FigureCanvasAgg(self.fig)
		self.canvas.draw()
		self.renderer = self.canvas.get_renderer()
		self.raw_data = self.renderer.tostring_rgb()

	def draw(self, screen):
		# self.kp_slider.
		size = self.canvas.get_width_height()
		surf = pg.image.fromstring(self.raw_data, size, "RGB")
		screen.blit(surf, (0, 400))
