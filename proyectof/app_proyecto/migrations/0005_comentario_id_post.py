# Generated by Django 4.0.5 on 2022-06-25 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_proyecto', '0004_alter_avatar_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='id_post',
            field=models.ForeignKey(default=46, on_delete=django.db.models.deletion.CASCADE, to='app_proyecto.post'),
            preserve_default=False,
        ),
    ]
