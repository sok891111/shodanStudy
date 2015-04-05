#!/usr/bin/env python
import Queue
import threading
import urllib2
import httputil;

hosts = []

queue = Queue.Queue()

class ThreadUrl(threading.Thread):
	"""Threaded Url Grab"""
	def __init__(self, queue ):
		threading.Thread.__init__(self)
		self.queue = queue

	def run(self):
		while True:
			#grabs host from queue
			request = self.queue.get()

			#grabs urls of hosts and prints first 1024 bytes of page
			response = httputil._http_request(request)
			if request.callback is not None:
				request.callback(response)

		#signals to queue job is done
		self.queue.task_done()


def set_asyn(request):
	hosts.append(request)

def start():
	for request in hosts:
		queue.put(request)
		t = ThreadUrl(queue)
		t.setDaemon(True)
		t.start()
	queue.join()


