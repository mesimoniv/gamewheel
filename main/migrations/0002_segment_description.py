# Generated by Django 2.2.5 on 2019-10-01 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='segment',
            name='description',
            field=models.CharField(default='You have won ', max_length=400),
        ),
    ]
