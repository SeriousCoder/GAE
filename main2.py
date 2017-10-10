import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import users

class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'project.html')
        self.response.out.write(template.render(path, template_values))
		
application = webapp2.WSGIApplication([('/', MainPage)])