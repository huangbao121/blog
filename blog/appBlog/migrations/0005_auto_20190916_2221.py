# Generated by Django 2.2.1 on 2019-09-16 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0004_auto_20190916_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='click',
            field=models.IntegerField(default=0, verbose_name='点击率'),
        ),
        migrations.AddField(
            model_name='article',
            name='recommend',
            field=models.IntegerField(default=0, verbose_name='推荐'),
        ),
    ]