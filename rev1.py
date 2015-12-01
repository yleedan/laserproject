import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)

class times:
	def __init__(self):
		self.time0 = time.time()
		self.time1 = 0
		self.time2 = 0
		self.time3 = 0
		self.ready = 0
		self.diff1 = 0
		self.diff2 = 0
		self.v1 = 0
		self.v2 = 0
		self.vdiff = 0
		self.a1 = 0
		self.d1 = 0.07
		self.d2 = 0.07
		print('Set up complete! Waiting for drop...')

	def Input_1(self, channel):
		self.time1 = time.time()
		
	def Input_2(self, channel):
		self.time2 = time.time()
		
	def Input_3(self, channel):
		self.time3 = time.time() 	
		self.diff2 = self.time3 - self.time2
		self.diff1 = self.time2 - self.time1
		self.dt = (self.diff1 + self.diff2) / 2
		self.v1 = float(self.d1) / self.diff1
		self.v2 = float(self.d2) / self.diff2
		self.vdiff = self.v2 - self.v1
		self.a1 = self.vdiff / self.dt
		print('%r seconds have passed between laser 1 and laser 2 breaking.' % self.diff1)
		print('%r seconds have passed between laser 2 and laser 3 breaking.' % self.diff2)
		print('Average velocity between lasers 1 and 2 is %r m/s.' % self.v1)
		print('Average velocity between lasers 2 and 3 is %r m/s.' % self.v2)
		print('Average acceleration between lasers 1 and 3 is %r m/s^2.' % self.a1)
		print('---------------')
timer = times()
GPIO.add_event_detect(17, GPIO.RISING, callback=timer.Input_1, bouncetime = 300)
GPIO.add_event_detect(27, GPIO.RISING, callback=timer.Input_2, bouncetime = 300)
GPIO.add_event_detect(22, GPIO.RISING, callback=timer.Input_3, bouncetime = 300)

while True:
	time.sleep(60)
