# Generated by Django 4.2 on 2024-05-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widget', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='css',
            field=models.TextField(default=''),
        ),
    ]