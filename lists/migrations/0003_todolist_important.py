# Generated by Django 3.0.8 on 2020-08-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20200801_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='important',
            field=models.BooleanField(default=False),
        ),
    ]
