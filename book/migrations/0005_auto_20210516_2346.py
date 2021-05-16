# Generated by Django 3.1.2 on 2021-05-16 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20210516_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_uuid',
            field=models.UUIDField(default='2d31862d-9687-40f7-ac33-2b665ee926ea', verbose_name='PublishCompany'),
        ),
        migrations.AlterField(
            model_name='publishcompany',
            name='pub_company',
            field=models.CharField(max_length=15, unique=True, verbose_name='Publishing Company Name'),
        ),
        migrations.AlterField(
            model_name='publishcompany',
            name='pub_uuid',
            field=models.UUIDField(default='dfce3e46-9fc3-43cc-b9b6-73f4e6954175', primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]