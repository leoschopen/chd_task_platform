# Generated by Django 2.0.6 on 2019-12-01 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_platform', '0004_task_task_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_class',
            field=models.CharField(default='赏金模式', max_length=48),
        ),
    ]
