# Generated by Django 2.2.6 on 2021-01-12 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_img', models.ImageField(blank=True, default='avatar/avatar.jpg', upload_to='avatar/', verbose_name='头像')),
                ('user_desc', models.CharField(blank=True, default='', max_length=50, verbose_name='个性签名')),
                ('user_content', models.TextField(blank=True, default='', verbose_name='个人介绍')),
                ('user_type', models.CharField(choices=[('GR', '个人'), ('QY', '企业'), ('SH', '社会团体')], default='GR', max_length=5, verbose_name='用户类型')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='手机号')),
                ('add_date', models.DateField(auto_now_add=True, verbose_name='注册日期')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户中心',
                'verbose_name_plural': '用户中心',
            },
        ),
    ]
