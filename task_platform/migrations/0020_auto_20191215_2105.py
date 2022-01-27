# Generated by Django 2.0.6 on 2019-12-15 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_platform', '0019_withdraw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdraw',
            name='state',
            field=models.CharField(blank=True, choices=[('发起', 'start'), ('确认', 'confirmed'), ('完成', 'complete'), ('取消', 'cancel')], max_length=20, null=True),
        ),
    ]
