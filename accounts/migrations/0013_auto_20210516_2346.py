# Generated by Django 3.1.2 on 2021-05-16 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210516_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default='72afa9f6-68cb-4da1-a7a5-ed7da99d7f4e', primary_key=True, serialize=False),
        ),
    ]
