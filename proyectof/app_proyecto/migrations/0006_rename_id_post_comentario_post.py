# Generated by Django 4.0.5 on 2022-06-27 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_proyecto', '0005_comentario_id_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='id_post',
            new_name='post',
        ),
    ]