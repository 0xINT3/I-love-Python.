import random
import urllib
string = ''

def download_image(url):
	name = random.randrange(1,500)
	full = str(name) + '.jpg'
	urllib.urlretrieve(url,full)

download_image('https://images.techhive.com/images/article/2016/07/linux-terminal-1-100669790-gallery.idge.jpg')
