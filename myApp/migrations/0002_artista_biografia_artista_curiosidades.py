# Generated by Django 5.1.3 on 2024-11-14 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artista',
            name='biografia',
            field=models.TextField(default='bio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artista',
            name='curiosidades',
            field=models.TextField(null=True),
        ),
    ]
