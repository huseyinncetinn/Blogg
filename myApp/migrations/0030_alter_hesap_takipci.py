# Generated by Django 3.2.16 on 2023-01-11 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0029_alter_hesap_takipci'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hesap',
            name='takipci',
            field=models.ManyToManyField(blank=True, related_name='_myApp_hesap_takipci_+', to='myApp.Hesap'),
        ),
    ]