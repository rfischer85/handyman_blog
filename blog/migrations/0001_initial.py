# Generated by Django 4.2.1 on 2023-06-19 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('text', models.TextField(max_length=600, null=True)),
                ('approved', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(help_text='The date & time this article was published', unique_for_date='published')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', help_text='Set to "published" to make this post publicly visible.', max_length=10)),
                ('content', models.TextField()),
                ('published', models.DateTimeField(blank=True, help_text='The date & time this article was published', null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('comment', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.comment')),
                ('topics', models.ManyToManyField(related_name='blog_posts', to='blog.topic')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
    ]
