# Generated by Django 4.0.4 on 2022-04-24 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.URLField(null=True),
        ),
    ]