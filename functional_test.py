# functional_test.py тестирование Джанго
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		self.fail('Закончить тест')
		# Ей сразу же предлагается ввести элемент списка
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)
		#Она набирает в текстовом поле "Купить павлиньи перья" (ее хобби вязание рыболовных мушек)
		inputbox.send_keys('Купить павлиньи перья')

		# Когда она нажимает enter страница обновляется и теперь страница содержит
		# "1:Купить павлиньи перья" в качестве элемента списка
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1:Купить павлиньи перья' for row in rows)
			)
		# Текстовое поле по-прежнему приглашает ее добаить еще один элемент. Она вводит
		# "Сделать мушку из павлиньих перьев"

		self.fail('Закончить тест!')


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