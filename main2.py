#! /usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import users

import os

class Question0(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "0",
			'someQuestion' : "Привет! Это небольшой интерактивный квест, в конце которого ты узнаешь много интересных фактах о «Норникеле» и не только – эти факты помогут тебе победить в лотерее, но кое-где придется подумать. Начнем с простенького: <br>2+2*2=?"}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))

class Question1(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "1",
			'someQuestion' : "Что это? <br>15 16 18 15 10 12 6 13 30"}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
		
		
class Question2(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "2",
			'someQuestion' : "В одном мобильном телефоне содержится примерно 9мг палладия. Тони Старку потребовалось 1,6 грамм палладия, чтобы создать свой мини-реактор для Железного Человека. <br>Сколько телефонов ему понадобилось?"}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
		
class Question3(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "3",
			'someQuestion' : "Этот человек известен своей любовью к альтернативным источникам питания, а ещё он уничтожит ДВС и отправит нас на марс. Постарайся написать максимально точно по-русски имя этого человека."}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
		
class Question4(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "4",
			'someQuestion' : "В организме человека содержится примерно 1 Мега гекто деци нано грамм никеля. Так сколько миллиграмм никеля в теле человека? <br>В ответе только число."}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))

class Question5(webapp2.RequestHandler):
    def get(self):
	template_values = {
<<<<<<< HEAD
            'id': "4",
			'someQuestion' : "Найдите <i>cos a</i> , если <i>sin 2a = -0.96</i> и <i>-1 < sin a < 0</i>. "}
=======
            'id': "5",
			'someQuestion' : "Именно эти годовщины совместной жизни у супругов называются никелевой свадьбой. Чтобы получить ответ определите в какой точке будет находиться вершина параболы: <br> <i>Y =-2x<sup>2</sup>+48x-260</i>. <br>Ответ - два числа через запятую без пробелов"}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
	
class Question6(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "6",
			'someQuestion' : "Решите уравнение (УРАВНЕНИЕ)"}
>>>>>>> ef721d615a91dab744262fb0be7da3d58f5d3d1f
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
		
class Question7(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "7",
			'someQuestion' : "На заводе работают три смены, которые сменяют друг друга. Каждая смена работает по 8 часов. Первая смена выходит на работу в 10 утра, во сколько заканчивается рабочий день у 3 смены?"}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
		
class Question8(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "8",
			'someQuestion' : "Именно столько миллиардов долларов составила выручка компании «Норникель» в первом полугодии 2017 года. Чтобы узнать ответ запиши через запятую (без пробелов) период и группу, в которых находится Аргон."}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
		
application = webapp2.WSGIApplication([('/Uyolanan'		, Question0),
															('/Swemankar'	, Question1),
															('/Lanadl'			, Question2),
															('/Slarrac'			, Question3),
															('/Jallly'				, Question4),
															('/Gixass'			, Question5),
															('/Vaula'			, Question6),
															('/Pona'				, Question7),
															('/Cameeroya'	, Question8)])