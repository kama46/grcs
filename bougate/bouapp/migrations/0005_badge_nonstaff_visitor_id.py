# Generated by Django 4.1 on 2022-08-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bouapp', '0004_remove_badge_nonstaff_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge_nonstaff',
            name='visitor_ID',
            field=models.CharField(default='000', max_length=255),
        ),
    ]
