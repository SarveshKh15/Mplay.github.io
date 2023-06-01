# Generated by Django 3.2.15 on 2023-04-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='songs/cat_imgs')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_name', models.CharField(max_length=50)),
                ('music_singer', models.CharField(max_length=50)),
                ('music_movie', models.CharField(max_length=100)),
                ('music_durations', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='songs/covers')),
                ('audio', models.FileField(upload_to='songs/audio')),
                ('pub_date', models.DateField()),
            ],
        ),
    ]