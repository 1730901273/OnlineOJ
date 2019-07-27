# Generated by Django 2.2.3 on 2019-07-09 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, db_column='phone', default=None, max_length=11, null=True, unique=True, verbose_name='电话号码')),
                ('email', models.EmailField(max_length=254, verbose_name='电子邮箱')),
                ('username', models.CharField(db_column='username', max_length=20, unique=True, verbose_name='用户')),
                ('password', models.CharField(db_column='password', max_length=20, verbose_name='密码')),
                ('src', models.TextField(verbose_name='用户简介')),
                ('isActive', models.BooleanField(default=True, verbose_name='启用/禁用')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='QuestionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('now_time', models.TimeField(db_column='now_time', verbose_name='提交时间')),
                ('AC', models.TextField(db_column='AC')),
                ('time', models.IntegerField(verbose_name='耗时')),
                ('memory', models.IntegerField(verbose_name='耗内存')),
                ('text_show', models.TextField(verbose_name='提示信息')),
                ('programming', models.CharField(db_column='program', max_length=20, verbose_name='编程语言')),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Questions.Questions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Users')),
            ],
            options={
                'verbose_name': '我的题库',
                'verbose_name_plural': '我的题库',
                'db_table': 'QuestionInfo',
            },
        ),
    ]