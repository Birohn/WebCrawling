import os

def generate_project_dir(directory):
	if not os.path.exists(directory):
		print('Creating project' + directory)
		os.makedirs(directory)

def generate_files(directory, url):
	queue = directory + '/queue.txt'
	crawled = directory + '/crawled.txt'
	if not os.path.isfile(queue):
		write_to_file(queue, url)
		print('Generating queue.txt')
	if not os.path.isfile(crawled):
		write_to_file(crawled,"")
		print('Generating crawled.txt')
		
def write_to_file(directory,data):
	with open(directory,'w',encoding='utf-8') as f:
		f.write(data + '\n')
		
def append_to_file(directory, data):
	with open(directory,'a',encoding='utf-8') as f:
		f.write(data + '\n')
		
def delete_file_content(directory):
	with open(directory,'w') as f:
		pass
		
def file_to_set(file):
	links = set()
	with open(file, 'rt',encoding='utf-8') as f:
		for lines in f:
			links.add(lines.replace('\n',''))
	return links

def set_to_file(set, file):
	if set is not None:
		generator=list((links for links in set if links is not None and 'http' in links))
		if generator is not None:
			delete_file_content(file)
			for links in generator:
				append_to_file(file,links)
		else:
			pass
	else:
		pass
