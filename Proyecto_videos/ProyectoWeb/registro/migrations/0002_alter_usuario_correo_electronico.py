# Generated by Django 4.2.8 on 2024-12-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='correo_electronico',
            field=models.EmailField(default='example@example.com', max_length=254, unique=True),
        ),
    ]
