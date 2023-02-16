from init_stopwatch import Stopwatch_init
from init_timer import Timer_init
from init_watch import Watch_init

class Init():
	@classmethod
	def watch(self):
		Watch_init()

	@classmethod
	def stopwatch(self):
		Stopwatch_init()

	@classmethod
	def timer(self):
		Timer_init()
