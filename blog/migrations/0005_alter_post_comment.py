# Generated by Django 4.2.1 on 2023-06-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_comment_post_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.ManyToManyField(default='', related_name='comments', to='blog.comment'),
        ),
    ]
