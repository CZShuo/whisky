# Generated by Django 2.1.7 on 2019-06-21 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiskydatabase', '0015_auto_20190621_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whiskyinfo',
            name='casktype',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
