#!/usr/bin/python
import time
import json
import logging
import requests
import requests_cache
from requests.exceptions import Timeout, HTTPError

requests_cache.install_cache('baseapi_cache')
LOGGER = logging.getLogger('baseapi')
# requests log is by default set to INFO mode and a little too verbose
requests_log = logging.getLogger("requests")
requests_log.setLevel(logging.WARNING)

API_QUERY_BASE_URL = 'http://somedomain/someroute'
API_KEY = 'mykey'
API_SECRET = 'mysecretkey'

class BaseAPI(object):
	"""
	Constraints:
	-Caching in accordance with HTTP response headers
	-Rate limit: 5 requests per originating IP address per second, averaged over a 5 minute period, 
	"""
	def __init__(self, query_base_url=API_QUERY_BASE_URL, api_key=API_KEY, api_secret_key=API_SECRET):
		self.delay = 0.2 # min seconds between requests
		if not hasattr(self, 'last_request_time'):
			self.last_request_time = {}

		self.query_base_url = query_base_url
		self.api_key = API_KEY
		self.secret = api_secret_key
		self.headers = {'Accept': 'application/json',
				'User-Agent': 'python-requests/2.2.1'
		}
		
	def _throttle(self):
		""" 
		Will sleep for self.delay seconds before returning 
		"""
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
		"""
		self._throttle()
		payload = self._get_payload(**query_params)
		response = None
		try:
			response = requests.get(self.query_base_url, params=payload, headers=self.headers, timeout=timeout)
			try:
				response.raise_for_status()
			except HTTPError:
				LOGGER.error("Request responded with status code: %s" % (response.status_code))

		except Timeout:
			LOGGER.error("Request timed out after %s seconds" % timeout)

		if response:
			# return raw json string
			return response.json()
		else:
			return None


