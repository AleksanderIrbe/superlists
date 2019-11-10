# functional_test.py тестирование Джанго
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	'''тест нового посетителя'''
	def setUp(self):
		'''установка'''
		self.browser = webdriver.Firefox()

	def tearDown(self):
		'''демонтаж'''
		self.browser.quit()

	def test_can_start_a_list_and_retrive_it_later(self):
		'''тест:можно начать список и получить его позже'''
		#Эдит слышала про крутое новое онлайн-приложение со списком
		# неотложных дел. Она решает оценить его домашнюю страницу
		self.browser.get('http://localhost:8000')

		# Она видит, что заголовок и шапка страницы говорят о списках неотложных дел
		self.assertIn('To-Do', self.browser.title)
		self.fail('Закончить тест')
		# Ей сразу же предлагается ввести элемент списка

if __name__ == '__main__':
	unittest.main(warnings='ignore')		




browser = webdriver.Firefox()



# #Эдит слышала про крутое новое онлайн-приложение со списком
# # неотложных дел. Она решает оценить его домашнюю страницу
# browser.get('http://localhost:8000')

# # проверка запускается ли Джанго
# assert 'Django' in browser.title
# # Она видит, что заголовок и шапка страницы говорят о списках неотложных дел
# assert 'To-Do' in browser.title

# # Ей сразу же предлагается ввести элемент списка
# #Она набирает в текстовом поле "Купить павлиньи перья" (ее хобби вязание рыболовных мушек)
# # Когда она нажимает enter страница обновляется и теперь страница содержит
# # "1:Купить павлиньи перья" в качестве элемента списка
# browser.quit()