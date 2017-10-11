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
			'someQuestion' : "Привет! Это небольшой интерактивный квест, в конце которого ты узнаешь много интересных фактов о Генеральном партнере форума - компании \"Норникель\" <br>Читай внимательно!<br>Полученная информация станет ключевым фактором твоей победы в викторине от компании, которая пройдёт в 17:30 на сцене после мастер-класса!<br>Начнем с простенького: <br>2+2*2=?"}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))

class Question1(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "1",
			'someQuestion' : "Ура! Ты нашёл ещё один код!<br>Но расслабляться рано, давай лучше разгадаем, что здесь зашифровано? <br>15 16 18 15 10 12 6 13 30 "}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
		
		
class Question2(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "2",
			'someQuestion' : "Ты настоящий Шерлок! Уже 3-й факт почти в твоих руках!<br>Но сначала задачка :)<br>В одном мобильном телефоне содержится примерно 9мг палладия. Тони Старку потребовалось 1,6 грамм палладия, чтобы создать свой мини-реактор для Железного Человека. <br>Сколько телефонов ему понадобилось?"}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
		
class Question3(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "3",
			'someQuestion' : "Мы рады, что ты снова с нами!<br>Следующий вопрос:<br>Назови имя и фамилию человека, известного своей любовью к альтернативным источникам питания. Подсказка: он хочет уничтожить ДВС и отправить человечество на Марс!<br>P.S. Пиши только русскими буквами и без ошибок!"}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
		
class Question4(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "4",
			'someQuestion' : "Ты уже знаешь больше половины фактов, но ещё не все :) Решай скорее задачку!<br>В организме человека содержится примерно 1 Мега гекто деци нано грамм никеля. Так сколько миллиграмм никеля в теле человека? <br>В ответе укажи только число."}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))

class Question5(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "5",
			'someQuestion' : "Ты уже почти на финале!<br>Итак, снова задачка:<br>Именно эти годовщины совместной жизни у супругов называются никелевой свадьбой. Чтобы получить ответ, необходимо определить, в какой точке будет находиться вершина параболы: <br>Y =-2x2+48x-260. <br>В ответе укажи два числа через запятую и без пробелов"}
        path = os.path.join(os.path.dirname(__file__), 'foo.html')
        self.response.out.write(template.render(path, template_values))
	
class Question6(webapp2.RequestHandler):
    def get(self):
	template_values = {
            'id': "6",
			'someQuestion' : "Финал уже близко и пора дать тебе задачку посложнее!<br>Найдите cos a , если sin 2a = -0.96 и -1 < sin a < 0."}
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