# Generated by Django 4.1.2 on 2022-10-10 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='Date',
            field=models.DateField(default='1901-03-22'),
            preserve_default=False,
        ),
    ]