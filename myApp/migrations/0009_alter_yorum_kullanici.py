# Generated by Django 3.2.16 on 2022-11-20 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0008_remove_yorum_isim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yorum',
            name='kullanici',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]