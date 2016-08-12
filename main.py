# coding: utf-8

import sys
import requests 
from bs4 import BeautifulSoup
import time


#добавляет в PYTHONPATH путь поиска модулей *.py 
#и main.py, запускающего программу
sys.path.append('C:\\Users\\олег\\Python34\\requestsAndSoup\\fbi.gov\\')
sys.path.append('C:\\Users\\олег\\Python34\\requestsAndSoup\\fbi.gov\\modules')

#1   получим исходный код
from sourceIntoString import source #теперь есть строка исходного кода

#2. надо вызвать функцию из writeInFile.py для записи исходного кода в файл
import writeInFile

#3. вызвать getLinks(), записывающую все ссылки в нужном поле сайта
import getLinks





