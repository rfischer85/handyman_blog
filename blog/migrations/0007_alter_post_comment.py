# Generated by Django 4.2.1 on 2023-06-19 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_comment_post_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.comment'),
        ),
    ]
