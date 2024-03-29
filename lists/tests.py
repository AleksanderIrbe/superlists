from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page

class  HomePageTest(TestCase):
	'''тест домашней страницы'''

# 	def test_root_url_resolves_to_home_page_view(self):
# 		'''тест:корневой url преобразуется в представление домашней страницы'''
# 		found = resolve('/')
# 		self.assertEqual(found.func, home_page)
	
# 	def test_home_page_returns_correct_html(self):
# 		'''тест: домашняя страница возвращает правильный html'''
# #		request = HttpRequest()
# 		response = self.client.get('/')
# 		#response = home_page(request)
# 		html = response.content.decode('utf8')
# 		# expected_html = render_to_string('home.html')
# 		# self.assertEqual(html, expected_html)

# 		self.assertTrue(html.startswith('<html>'))
# 		self.assertIn('<title>To-Do lists</title>', html)
# 		self.assertTrue(html.endswith('</html>'))

# 		self.assertTemplateUsed(response, 'home.html')

	def test_uses_home_template(self):
		'''тест: используется домашний шаблон '''
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')