import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import users

import os

class MainPage(webapp2.RequestHandler):
    def get(self):
	template_values = {
			'id': 1,
            'sometext': "Some text for test"}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
		
class CheckAnswer(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(
                'Check')
		
application = webapp2.WSGIApplication([('/', MainPage),
									   ('/checkAnswer/', CheckAnswer)])