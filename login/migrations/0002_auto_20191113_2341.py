# Generated by Django 2.0.6 on 2019-11-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=1, max_length=11, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='stu_id',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
