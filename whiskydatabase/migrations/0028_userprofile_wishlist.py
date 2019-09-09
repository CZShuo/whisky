# Generated by Django 2.2.4 on 2019-09-09 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import whiskydatabase.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('whiskydatabase', '0027_auto_20190903_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('whisky', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='whiskydatabase.WhiskyInfo')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.TextField(blank=True, null=True)),
                ('profilepic', models.ImageField(blank=True, null=True, upload_to=whiskydatabase.models.path_and_rename)),
                ('wishlist', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
