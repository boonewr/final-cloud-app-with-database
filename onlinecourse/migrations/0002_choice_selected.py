# Generated by Django 4.2.3 on 2023-07-16 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]
