#!/usr/bin/python
import time
import json
import logging
import requests
import requests_cache
from requests.exceptions import Timeout, HTTPError

requests_cache.install_cache('lastfm_cache')
LOGGER = logging.getLogger('lastfmAPI')
requests_log = logging.getLogger("requests")
requests_log.setLevel(logging.WARNING)

API_QUERY_BASE_URL = 'http://ws.audioscrobbler.com/2.0/'
API_KEY = 'aaa'
API_SECRET = 'bbb'

class lastfmAPI(object):
	"""
	Constraints:
	-Caching in accordance with HTTP response headers
	-Rate limit: 5 requests per originating IP address per second, averaged over a 5 minute period, 
	"""
	__shared_state = {}
	def __init__(self, query_base_url=API_QUERY_BASE_URL, api_key=API_KEY, api_secret_key=API_SECRET):
		# use shared state between object instances (setting up for multiprocessing)
		self.__dict__ = self.__shared_state
		self.delay = 0.2 # min seconds between requests
		if not hasattr(self, 'last_request_time'):
			self.last_request_time = {}

		self.query_base_url = query_base_url
		self.api_key = api_key
		self.secret = api_secret_key
		self.headers = {'Accept': 'application/json',
				'User-Agent': 'python-requests/2.2.1'
		}
		
	def _throttle(self):
		""" Will sleep for self.delay seconds before returning """
		now = time.time()
		if (self.query_base_url in self.last_request_time and 
		    (time.time() - self.last_request_time[self.query_base_url] < self.delay)):
			self.throttle_time = (self.delay -
					     (now - self.last_request_time[self.query_base_url]))
			LOGGER.debug("Throttle: Sleeping for %s seconds" % self.throttle_time)
			time.sleep(self.throttle_time)
		self.last_request_time[self.query_base_url] = now

	def _get_payload(self, **params):
		payload = {
			'api_key': self.api_key,
			'format': 'json',
		}
		payload.update(**params)
		return payload
		
	def query(self, timeout=3, **query_params):
		"""
		TODO: add better error handling for 502 errors...
		TODO: update response error codes
		"""
		self._throttle()
		payload = self._get_payload(**query_params)
		response = None
		try:
			response = requests.get(self.query_base_url, params=payload, headers=self.headers, timeout=timeout)
			try:
				response.raise_for_status()
			except HTTPError:
				if response.status_code == 403:
					LOGGER.error("Request Rate Limit Reached. Sleeping for 10s")
					# try again after waiting for 10s
					time.sleep(10)
					response = self.query(query_str)
				elif response.status_code == 502:
					LOGGER.error("Bad Gateway Error (502) fetching '%s'." % response.url)
					time.sleep(1)
					# try again... ??
					#response = self.query(query_str)
				else:
					LOGGER.error("Request responded with status code: %s" % (response.status_code))
		except Timeout:
			LOGGER.error("Request timed out after %s seconds" % timeout)
		if response:
			# return raw json string so response can be hashed in memoize
			return response.json()
		else:
			return None

	def get_top_artists(self, pages=1):
		top_artists = []
		for page in range(pages):
			q = {
				'page': page+1,
				'method': 'chart.getTopArtists'
			}
			top_artist_resp = self.query(**q)
			top_artists.extend(top_artist_resp['artists']['artist'])
		return top_artists

	def get_top_tags(self, mbid):
		q = {
			'method': 'artist.getTopTags',
			'mbid' : mbid
		}
		top_tags = self.query(**q)
		try:
			return top_tags['toptags']['tag']
		except KeyError:
			return {}

	def get_tag_similar(self, tag):
		q = {
			'method': 'tag.getSimilar',
			'tag': tag
		}
		similar_tags = self.query(**q)
		try:
			return similar_tags['similartags']['tag']
		except KeyError:
			return []

	def get_tag_desc(self, tag):
		q = {
			'method': 'tag.getInfo',
			'tag': tag
		}
		tag_info = self.query(**q)
		try:
			return tag_info['tag']['wiki']['summary']
		except TypeError:
			return None

	def sanitize_tag_name(self, tag):
		"""
		Consider doing more string sanitization here, 
		removing punctuation, etc.
		"""
		return tag.lower()

	def get_all_top_tags(self, top_artists, top_artists_mbids):
		all_tags = {}
		for artist, mbid in zip(top_artists, top_artists_mbids):
			top_tags_mapped = {}
			top_tags = self.get_top_tags(mbid)
			for top_tag in top_tags:
				name = self.sanitize_tag_name(top_tag['name'])
				# don't include tags that have fewer than 5 counts
				if int(top_tag.values()[0]) < 5: 
					continue
				top_tags_mapped[name] = 1

			all_tags[artist] = top_tags_mapped

		return all_tags

