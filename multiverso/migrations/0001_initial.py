# Generated by Django 5.1 on 2024-09-18 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventoNoCanonico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.IntegerField()),
                ('nombre', models.CharField(max_length=215)),
                ('imagen1', models.CharField(default='default_image.jpg', max_length=215)),
                ('imagen2', models.CharField(default='default_image.jpg', max_length=215)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
