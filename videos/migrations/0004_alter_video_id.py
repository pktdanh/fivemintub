# Generated by Django 4.0.5 on 2022-07-11 03:00

from django.db import migrations
import flax_id.django.fields


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_alter_video_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='id',
            field=flax_id.django.fields.FlaxId(editable=False, max_length=16, primary_key=True, serialize=False),
        ),
    ]
