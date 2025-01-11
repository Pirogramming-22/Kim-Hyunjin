# Generated by Django 5.1.4 on 2025-01-09 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rate',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='review',
            name='written_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='actor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='director',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='review',
            name='genre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
