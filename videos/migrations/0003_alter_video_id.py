# Generated by Django 4.0.5 on 2022-07-11 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_alter_video_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
