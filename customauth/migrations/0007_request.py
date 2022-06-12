# Generated by Django 4.0.5 on 2022-06-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0006_alter_customuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="Ім'я")),
                ('email', models.EmailField(max_length=254, verbose_name='Електронна пошта')),
                ('subject', models.CharField(max_length=100, verbose_name='Тема')),
                ('message', models.TextField(verbose_name='Повідомлення')),
            ],
            options={
                'verbose_name': 'Запит',
                'verbose_name_plural': 'Запити',
            },
        ),
    ]
