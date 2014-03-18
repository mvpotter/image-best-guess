import requests

from html.parser import HTMLParser
from random import choice


class BestGuessHTMLParser(HTMLParser):
	'''
	Retrieves <a class="qb-b"> element content that refers to best guess for image.
	'''
	BEST_GUESS_TAG = 'a'
	BEST_GUESS_TAG_CLASS = 'qb-b'

	__result = None
	__use = False
	
	def handle_starttag(self, tag, attrs):
		attributes = dict(attrs)
		if tag == self.BEST_GUESS_TAG and attributes.get('class', '') == self.BEST_GUESS_TAG_CLASS:
			self.__use = True
	def handle_data(self, data):
		if self.__use:
			self.__result = data
			self.__use = False

	def get_result(self):
		return self.__result

class ImageBestGuessFinder():
	'''
	Retrieves best guess for an image.
	'''

	_UAS = [
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.76 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.102 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.102 Safari/537.36',
	'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:26.0) Gecko/20100101 Firefox/26.0',
	'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0',
	'Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53',
	'Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0',
	'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.76 Safari/537.36'
	]

	_HEADERS = {
	'User-Agent': choice(_UAS),
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Connection': 'close',
	'DNT': '1'
	}

	_SEARCH_QUERY = {'image_url': '', 'hl' : 'en'}
	_SEARCH_URL = 'http://www.google.com/searchbyimage';

	def find(self, image_url):
		self._HEADERS['User-Agent'] = choice(self._UAS)
		self._SEARCH_QUERY['image_url'] = image_url
		try:
			r = requests.get(self._SEARCH_URL, headers=self._HEADERS, params=self._SEARCH_QUERY, timeout=3.0)
		except requests.exceptions.Timeout:
			print ('Request timeout reached')
			return None
		if r.ok:
			parser = BestGuessHTMLParser(strict=False)
			parser.feed(r.text);
			return parser.get_result()
		else:
			print ('Unable to get result from google')
			return None

if __name__ == "__main__":
	import sys

	if len(sys.argv) > 1:
		finder = ImageBestGuessFinder()
		print(finder.find(sys.argv[1]))
	else:
		print ('Usage: image_best_guess.py image_url')