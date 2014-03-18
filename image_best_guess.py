from urllib.request import FancyURLopener
import urllib.parse
import re

class CustomUrlOpener(FancyURLopener):
	version = r'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'	

# TODO: improve request to get result from google
query = urllib.parse.urlencode({'image_url': 'http://www.airpano.com/files/Barcelona-Spain/image1a.jpg'})
url = 'http://www.google.com/searchbyimage?hl=en&{}'.format(query);

urlOpener = CustomUrlOpener()
result = urlOpener.open(url).read().decode('utf-8');

pattern = re.compile(r'Best')
m = pattern.search(result)

print ('Best' in result)