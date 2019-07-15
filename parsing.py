from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
def simple_get(url):
	try:
		with closing(get(url, stream=True)) as resp:
			if is_good_response(resp):
				return resp.content
			else:
				return None
				
	except (RequestException,KeyError) as e:
		log_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None
	
def is_good_response(resp):
	content_type = resp.headers['Content-Type'].lower()
	return(resp.status_code == 200 and content_type is not None and content_type.find('html') >-1)
	
def log_error(e):
	print(e)
	
def grab_links(url):
	links= set()
	connect=simple_get(url)
	try:
		soup = BeautifulSoup(connect,'html.parser')
		for link in soup.find_all('a'):
			links.add(link.get('href'))
		return links
	except TypeError:
		print('Cannot access page')
		return links

