# Generated by Django 4.2.2 on 2023-06-23 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='abcdef', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
