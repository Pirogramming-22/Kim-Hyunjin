# Generated by Django 5.1.5 on 2025-01-20 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='clicked',
            field=models.BooleanField(default=False, verbose_name='체크여부'),
        ),
    ]
