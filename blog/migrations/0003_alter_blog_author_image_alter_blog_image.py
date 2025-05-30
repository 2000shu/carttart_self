# Generated by Django 5.1.5 on 2025-03-28 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_blog_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author_image',
            field=models.ImageField(blank=True, default='images/author_images/default_author_image.png', null=True, upload_to='blog/static/images/author_images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blog/static/images/blog_images/'),
        ),
    ]
