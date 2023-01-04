from django.test import TestCase
from django.contrib.auth import authenticate, get_user_model
from todo.models import Todo

class LoginTest(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='John', password='s8M7dh6GmFc')
        self.user.save()
    
    def tearDown(self):
        self.user.delete()
    
    def test_correct(self):
        user = authenticate(username='John', password='s8M7dh6GmFc')
        self.assertTrue((user is not None) and user.is_authenticated)
    
    def test_wrong_username(self):
        user = authenticate(username='Maria', password='s8M7dh6GmFc')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='John', password='369DGvgbvV7W')
        self.assertFalse(user is not None and user.is_authenticated)


class TodoTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='John', password='s8M7dh6GmFc')
        self.user.save()
        self.todo = Todo(user=self.user, title='title', memo='memo', important=False)
    
    def tearDown(self):
        self.user.delete()
    
    def test_read_todo(self):
        self.assertEqual(self.todo.user, self.user)
        self.assertEqual(self.todo.title, 'title') and self.assertEqual(self.todo.memo, 'memo') \
            and self.assertEqual(self.todo.important, False)
    
    def test_update_todo_title(self):
        self.todo.title = 'new title'
        self.todo.save()
        self.assertEqual(self.todo.title, 'new title')

    def test_update_todo_memo(self):
        self.todo.memo = 'new memo'
        self.todo.save()
        self.assertEqual(self.todo.memo, 'new memo')
    
    def test_update_todo_important(self):
        self.todo.title = True
        self.todo.save()
        self.assertEqual(self.todo.title, True)