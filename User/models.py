# from django.contrib.auth.models import AbstractUser
from django.db import models
from Questions.models import Questions


# Create your models here.
# 用户的数据库模型
class Users(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, verbose_name="ID")
    # 电话号码
    phone = models.CharField(db_column='phone', unique=True, blank=True, null=True, default=None, max_length=11,
                             verbose_name='电话号码')
    # 电子邮箱
    email = models.EmailField(verbose_name='电子邮箱')
    # 用户名称
    username = models.CharField(db_column='username', unique=True, max_length=20, verbose_name='用户')
    # 用户密码
    password = models.CharField(db_column='password', max_length=20, verbose_name='密码')
    # 扩展用户头像字段
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', default='avatar/default.png',
                               verbose_name='头像', height_field=80, width_field=80)
    # 启用/禁用-BooleanField()，实现用户管理
    isActive = models.BooleanField(default=True, verbose_name='启用/禁用')

    # 后台管理的显示数据
    def __str__(self):
        return self.username

    def __repr__(self):
        return "<Users:%r>" % self.username

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']


# 创建用户的题库
class QuestionInfo(models.Model):
    # 关联关系:关联Users实体(一)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    # 关联关系:关联Questions实体(一)
    questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    # 提交时间
    now_time = models.TimeField(db_column='now_time', verbose_name='提交时间')
    # 用户最近提交的代码
    AC = models.TextField(db_column='AC')
    # 用时多少
    time = models.IntegerField(verbose_name='耗时')
    # 用内存多少
    memory = models.IntegerField(verbose_name='耗内存')
    # 如果ac，怎显示超过选手的百分比，否则输出错误信息
    text_show = models.TextField(verbose_name='提示信息')
    # 所用的编程语言
    programming = models.CharField(db_column='program', max_length=20, verbose_name="编程语言")

    class Meta:
        db_table = "QuestionInfo"
        verbose_name = '我的题库'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user
