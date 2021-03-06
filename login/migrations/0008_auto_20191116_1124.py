# Generated by Django 2.0.6 on 2019-11-16 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_user_money'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_sn', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='订单号')),
                ('trade_no', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='支付订单号')),
                ('pay_status', models.CharField(choices=[('TRADE_SUCCESS', '交易支付成功'), ('TRADE_CLOSED', '未付款交易超时关闭'), ('WAIT_BUYER_PAY', '交易创建'), ('TRADE_FINISHED', '交易结束'), ('paying', '待支付')], default='paying', max_length=40, verbose_name='订单状态')),
                ('order_mount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='充值金额')),
            ],
            options={
                'verbose_name': '充值订单',
                'verbose_name_plural': '充值订单',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='money',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User', verbose_name='用户'),
        ),
    ]
