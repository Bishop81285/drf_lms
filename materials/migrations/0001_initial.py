# Generated by Django 4.2.7 on 2023-11-07 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='course/', verbose_name='превью')),
                ('description', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='lesson/', verbose_name='превью')),
                ('video_url', models.URLField(blank=True, null=True, verbose_name='ссылка на видео')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
    ]