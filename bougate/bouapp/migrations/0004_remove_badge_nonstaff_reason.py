# Generated by Django 4.1 on 2022-08-17 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bouapp', '0003_alter_badge_nonstaff_badgeout_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badge_nonstaff',
            name='reason',
        ),
    ]
