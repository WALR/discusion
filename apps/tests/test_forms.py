from django.test import TestCase 

from apps.users.models import User
from apps.discuss.models import Question, Answer

class TestDiscuss(TestCase):

	def setUp(self):
		self.user = User.objects.create_superuser(username='Wil', email='wilfred@gmail.com', password='123')
		self.question = Question.objects.create(user=self.user,
				title='titulo', description ='descripcion')

	def test_createAnswer(self):
		user = self.client.login(username='Wil', password='123')
		self.assertTrue(user)
		self.assertEqual(Answer.objects.count(), 0)
		data = {
			'user' : self.user.id,
			'question' : self.question.id,
			'description': 'descripcion',
		}
		self.client.post('/pregunta/%s/' %self.question.slug, data)
		self.assertEqual(Answer.objects.count(), 1)