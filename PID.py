import time


class PID:
	def __init__(self):
		self.Kp = 0.0
		self.Ki = 0.0
		self.Kd = 0.0
		self.last_error = 0
		self.last_time = time.time()
		self.integral = 0
		self.p_enabled = True
		self.i_enabled = True
		self.d_enabled = True
		self.last_output = 0
		self.last_error = 0

	def reset_history(self):
		self.integral = 0
		self.last_error = 0
		self.last_output = 0
		self.last_time = time.time()

	def pid(self, input, setpoint):
		error = setpoint - input
		current_time = time.time()
		delta_time = current_time - self.last_time
		self.integral += error * delta_time
		derivative = (error - self.last_error)/delta_time
		output = 0
		if self.p_enabled:
			output += self.Kp*error
		if self.i_enabled:
			output += self.Ki*self.integral
		if self.d_enabled:
			output -= self.Kd*derivative
		self.last_error = error
		self.last_time = current_time
		self.last_output = output
		return output