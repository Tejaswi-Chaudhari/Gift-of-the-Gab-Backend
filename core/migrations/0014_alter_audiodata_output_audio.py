# Generated by Django 3.2.2 on 2021-07-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210629_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiodata',
            name='output_audio',
            field=models.FileField(default='', upload_to='output/audio'),
        ),
    ]
