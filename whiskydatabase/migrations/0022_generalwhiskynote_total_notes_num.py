# Generated by Django 2.2.4 on 2019-08-26 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiskydatabase', '0021_auto_20190826_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalwhiskynote',
            name='total_notes_num',
            field=models.IntegerField(default=0),
        ),
    ]
