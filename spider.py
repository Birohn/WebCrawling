#author: Byron Mouen
#The spider class which is responsible for
#grabbing the links and updating the queue
#and crawled files

from parsing import grab_links
from os_file import *
from urllib.request import urlopen

class Spider:
	folder_name=''
	base_url=''
	domain_name=''
	queue_file=''
	crawled_file=''
	queue=set()
	crawled=set()
	
	def __init__(self,folder_name,base_url,domain_name):
		Spider.folder_name = folder_name
		Spider.base_url = base_url
		Spider.domain_name = domain_name
		Spider.queue_file= folder_name +'/queue.txt'
		Spider.crawled_file= folder_name +'/crawled.txt'
		self.boot()
		self.crawl_page("First Spider", Spider.base_url)
		
	@staticmethod
	def boot():
		generate_project_dir(Spider.folder_name)
		generate_files(Spider.folder_name,Spider.base_url)
		Spider.queue=file_to_set(Spider.queue_file)
		Spider.crawled = file_to_set(Spider.crawled_file)
	@staticmethod
	def crawl_page(thread_name, page_url):
		if not page_url in Spider.crawled:
			print(thread_name + 'crawling ' + page_url)
			print('Queue ' + str(len(Spider.queue)) + ' | Cralwed ' + str(len(Spider.crawled)))
			Spider.add_links_to_queue(grab_links(page_url))
			Spider.queue.remove(page_url)
			Spider.crawled.add(page_url)
			Spider.update_files()
			
	@staticmethod
	def add_links_to_queue(links):
		for url in links:
			if url in Spider.queue:
				continue
			elif url in Spider.crawled:
				continue
			else:
				Spider.queue.add(url)
				
	@staticmethod
	def update_files():
		set_to_file(Spider.queue,Spider.queue_file)
		set_to_file(Spider.crawled,Spider.crawled_file)
			
	