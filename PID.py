import time


class PID:
	def __init__(self):
		self.Kp = 0.0
		self.Ki = 0.0
		self.Kd = 0.0
		self.last_error = 0
		self.last_time = time.time()
		self.integral = 0

	def pid(self, input, setpoint):
		error = setpoint - input
		current_time = time.time()
		delta_time = current_time - self.last_time
		self.integral += error * delta_time
		derivative = (error - self.last_error)/delta_time
		output = self.Kp*error + self.Ki*self.integral + self.Kd*derivative
		self.last_error = error
		return output