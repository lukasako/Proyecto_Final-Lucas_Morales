# Generated by Django 4.0.5 on 2022-06-22 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_proyecto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comentario',
        ),
    ]
