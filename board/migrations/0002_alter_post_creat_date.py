# Generated by Django 4.0.5 on 2022-06-25 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creat_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
