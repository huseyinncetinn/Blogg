# Generated by Django 3.2.16 on 2022-11-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='icerik',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
