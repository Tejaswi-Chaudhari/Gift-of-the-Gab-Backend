# Generated by Django 3.2.2 on 2021-05-23 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_card_exercise_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='audio',
            field=models.FileField(default='', upload_to='card/audio'),
        ),
        migrations.AlterField(
            model_name='card',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='card/images'),
        ),
        migrations.AlterField(
            model_name='history',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='card/images'),
        ),
    ]
