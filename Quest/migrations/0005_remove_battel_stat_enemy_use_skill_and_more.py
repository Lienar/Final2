# Generated by Django 5.1.1 on 2024-10-15 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quest', '0004_battel_stat_enemy_use_skill_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='battel_stat',
            name='Enemy_use_skill',
        ),
        migrations.RemoveField(
            model_name='battel_stat',
            name='Player_use_skill',
        ),
    ]
