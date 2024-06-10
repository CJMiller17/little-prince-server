# Generated by Django 5.0.6 on 2024-06-10 13:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profile_image', models.ImageField(upload_to='images/')),
                ('butterflies', models.BooleanField(blank=True)),
                ('elephants', models.IntegerField(blank=True)),
                ('games', models.TextField(blank=True)),
                ('fav_color', models.CharField(max_length=100)),
                ('birds_collected', models.IntegerField(blank=True)),
                ('score_little_prince', models.IntegerField(blank=True)),
                ('score_king', models.IntegerField(blank=True)),
                ('score_conceited_man', models.IntegerField(blank=True)),
                ('score_drunkard', models.IntegerField(blank=True)),
                ('score_business_man', models.IntegerField(blank=True)),
                ('score_lamplighter', models.IntegerField(blank=True)),
                ('score_geographer', models.IntegerField(blank=True)),
                ('score_earth', models.IntegerField(blank=True)),
                ('total_score', models.IntegerField(blank=True)),
                ('item_1', models.IntegerField(blank=True)),
                ('item_2', models.IntegerField(blank=True)),
                ('item_3', models.IntegerField(blank=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
