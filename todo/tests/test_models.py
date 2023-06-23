from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from todo.models import Todo


class TodoTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='John', password='s8M7dh6GmFc')
        self.user.save()
        self.todo = Todo(user=self.user, title='title', memo='memo', important=False, \
                        due_date=timezone.datetime.now(tz=timezone.utc)+timezone.timedelta(days=1))
    
    def tearDown(self):
        self.user.delete()
    
    def test_read_todo(self):
        self.assertEqual(self.todo.user, self.user)
        self.assertEqual(self.todo.title, 'title') and self.assertEqual(self.todo.memo, 'memo') \
            and self.assertEqual(self.todo.important, False) and self.assertEqual(self.todo.due_date, timezone.datetime.now(tz=timezone.utc)+timezone.timedelta(days=1))
    
    def test_update_todo_title(self):
        self.todo.title = 'new title'
        self.todo.save()
        self.assertEqual(self.todo.title, 'new title')

    def test_update_todo_memo(self):
        self.todo.memo = 'new memo'
        self.todo.save()
        self.assertEqual(self.todo.memo, 'new memo')
    
    def test_update_todo_important(self):
        self.todo.important = True
        self.todo.save()
        self.assertEqual(self.todo.important, True)

    def test_update_todo_due_date(self):
        due_date = timezone.datetime.now(tz=timezone.utc)+timezone.timedelta(days=2)
        self.todo.due_date = due_date
        self.todo.save()
        self.assertEqual(self.todo.due_date, due_date)