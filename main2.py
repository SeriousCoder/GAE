import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import users

class MainPage(webapp2.RequestHandler):
    def get(self):
	self.response.write(
            '<html><body>{}</body></html>'.format(greeting))
		
application = webapp2.WSGIApplication([('/', MainPage)])