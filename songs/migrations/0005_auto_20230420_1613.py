# Generated by Django 3.2.15 on 2023-04-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_auto_20230420_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlater',
            name='id',
        ),
        migrations.AddField(
            model_name='watchlater',
            name='watch_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
