# Generated by Django 2.1.3 on 2018-11-28 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True, null=True, verbose_name='Message')),
                ('created_time', models.DateTimeField(verbose_name='Comment creation time')),
                ('updated_time', models.DateTimeField(verbose_name='Comment update time')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='CommentPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='Comment Photo')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read_feed.Comment', verbose_name='Comment')),
            ],
        ),
        migrations.CreateModel(
            name='FBUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=80, unique=True, verbose_name='Facebook user ID')),
                ('user_name', models.CharField(max_length=80, verbose_name='User name')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=50, unique=True, verbose_name='Post ID')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Post message')),
                ('post_link', models.URLField(blank=True, max_length=250, null=True)),
                ('created_time', models.DateTimeField(verbose_name='Post creation time')),
                ('updated_time', models.DateTimeField(verbose_name='Post update time')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated at')),
                ('fbuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read_feed.FBUser', verbose_name='Facebook User')),
            ],
        ),
        migrations.CreateModel(
            name='PostPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='Post photo')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read_feed.Post', verbose_name='Post')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='fbuser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='read_feed.FBUser', verbose_name='Comment by'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read_feed.Post', verbose_name='Post'),
        ),
    ]