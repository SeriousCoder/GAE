import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import users

import os

class Question1(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "0",
			'someQuestion' : "В одном мобильном телефоне содержится примерно 9мг палладия. Тони Старку потребовалось 1,6 грамм палладия, чтобы создать свой мини-реактор для Железного Человека. Сколько телефонов ему понадобилось? \n 180тлф = 1,62 грамм"}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
		
class CheckAnswer(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(
                'Check')
		
application = webapp2.WSGIApplication([('/', Question1),
									   ('/checkAnswer/', CheckAnswer)])