# Generated by Django 2.2.4 on 2019-09-20 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiskydatabase', '0030_auto_20190916_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='whiskyinfo',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='whiskyinfo',
            name='slug',
            field=models.IntegerField(default='', editable=False, max_length=200),
        ),
    ]
