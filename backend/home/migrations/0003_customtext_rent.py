# Generated by Django 2.2.24 on 2021-09-19 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_customtext_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='rent',
            field=models.TextField(blank=True, null=True),
        ),
    ]
