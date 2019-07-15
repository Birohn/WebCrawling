#author:Byron Mouen
#main file of the program

import threading
from queue import Queue
from spider import Spider
from os_file import *
#folder name where the queue and crawled files will be stored
PROJECT_NAME ='steam'
#starting point
HOMEPAGE ='https://store.steampowered.com/'
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
#Number of thread varies on your cpu
NUMBER_OF_THREADS = 5
queue =Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)

def create_workers():
	for _ in range(NUMBER_OF_THREADS):
		t = threading.Thread(target=work)
		t.daemon = True
		t.start()
		
def work():
	while True:
		url = queue.get()
		Spider.crawl_page(threading.current_thread().name,url)
		queue.task_done()

def create_jobs():
	for link in file_to_set(QUEUE_FILE):
		queue.put(link)
	queue.join()
	crawl()


def crawl():
	queued_links = file_to_set(QUEUE_FILE)
	if len(queued_links) > 0:
		print(str(len(queued_links))+ ' links in the queue')
		create_jobs()
create_workers()
crawl()