# Generated by Django 4.0.5 on 2022-06-09 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
