# Generated by Django 3.2.13 on 2023-06-12 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todo_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='notify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
