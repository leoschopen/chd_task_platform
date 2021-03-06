# Generated by Django 2.0.6 on 2019-11-25 01:40

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(max_length=128)),
                ('receiver', models.CharField(blank=True, default='', max_length=128)),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
                ('people_needed', models.IntegerField(default=1)),
                ('people_now', models.IntegerField(default=0)),
                ('expected_time_consuming', models.DecimalField(decimal_places=1, default=0.0, max_digits=12)),
                ('task_description', models.CharField(default='None', max_length=50)),
                ('task_detail', ckeditor_uploader.fields.RichTextUploadingField(default='None')),
                ('task_state', models.CharField(choices=[('未开始', 'waitting'), ('进行中', 'processing'), ('中止', 'abort'), ('撤销', 'revoke'), ('超时', 'timeout'), ('完成', 'completed')], default='未开始', max_length=32)),
            ],
            options={
                'verbose_name': '任务',
                'verbose_name_plural': '任务',
                'ordering': ['pub_time'],
            },
        ),
        migrations.CreateModel(
            name='Task_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sig_tag', models.CharField(default='None', max_length=20)),
                ('task_id', models.IntegerField(default='0')),
            ],
            options={
                'verbose_name': '任务标签',
                'verbose_name_plural': '任务标签',
            },
        ),
        migrations.CreateModel(
            name='User_task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(default='0')),
                ('username', models.CharField(default='None', max_length=128)),
                ('description', models.CharField(max_length=50)),
                ('submit_money', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name': '用户任务报价',
                'verbose_name_plural': '用户任务报价',
            },
        ),
    ]
