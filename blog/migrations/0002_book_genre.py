# Generated by Django 2.2.7 on 2019-11-07 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
