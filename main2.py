#! /usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import users

import os

class Question1(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "0",
			'someQuestion' : "В одном мобильном телефоне содержится примерно 9мг палладия. Тони Старку потребовалось 1,6 грамм палладия, чтобы создать свой мини-реактор для Железного Человека. Сколько телефонов ему понадобилось?"}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
		
class Question2(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "1",
			'someQuestion' : "Этот человек известен своей любовью к альтернативным источникам питания, а ещё он уничтожит ДВС и отправит нас на марс"}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
		
class Question3(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "2",
			'someQuestion' : "В организме человека содержится примерно 1 гекто кило микро мега нано грамм никеля. Так сколько миллиграмм никеля в теле человека? Ответ только число."}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))

class Question4(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "3",
			'someQuestion' : "Именно эти годовщины совместной жизни у супругов называются никелевой свадьбой. Чтобы получить ответ определите в какой точке будет находиться вершина параболы (КВАДРАТИЧНАЯ ФУНКЦИЯ)"}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
	
class Question5(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "4",
			'someQuestion' : "Решите уравнение (УРАВНЕНИЕ)"}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
		
class Question6(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "5",
			'someQuestion' : "На заводе работают три смены, которые сменяют друг друга. Каждая смена работает по 8 часов. Первая смена выходит на работу в 10 утра, во сколько заканчивается рабочий день у 3 смены?"}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
		
application = webapp2.WSGIApplication([('/Lanadl'	, Question1),
									   ('/Slarrac'	, Question2),
									   ('/Jallly'	, Question3),
									   ('/Gixass'	, Question4),
									   ('/Vaula'	, Question5),
									   ('/Pona'		, Question6),])