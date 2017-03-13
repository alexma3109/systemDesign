from threading import Thread, Lock
import time
import random

queue = []
lock = Lock()

class ProducerThead(Thread):
	def run(self):
		nums = range(5)
		global queue
		while True:
			num = random.choice(nums)
			lock.acquire()
			queue.append(num)
			print "Produced", num
			lock.release()
			time.sleep(random.random() * 2)

class ConsumerThread(Thread):
	def run(self):
		global queue
		while True:
			while not queue:
				print "Nothing in queue"
				time.sleep(random.random());
				continue
			lock.acquire()
			num = queue.pop(0)
			print "Consumed", num
			lock.release()
			time.sleep(random.random())

ProducerThead().start()
ConsumerThread().start()
