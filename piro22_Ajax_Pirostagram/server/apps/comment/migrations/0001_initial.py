# Generated by Django 5.1.5 on 2025-01-19 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='수정일')),
                ('created_date', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='작성일')),
                ('content', models.TextField(verbose_name='댓글 내용')),
                ('like', models.IntegerField(default=0, verbose_name='좋아요 수')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
        ),
    ]
