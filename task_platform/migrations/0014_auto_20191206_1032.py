# Generated by Django 2.0.6 on 2019-12-06 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_platform', '0013_auto_20191206_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatinfo',
            name='send_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
