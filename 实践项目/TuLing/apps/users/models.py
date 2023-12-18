from django.db import models
# 使用django自带的 user 模型类（密码加密功能）
# AbstractUser是User继承的父类
# 这里继承后使用的就是其中的字段与方法（详细关系可以查看源码）
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # unique 唯一不可重复
    mobile = models.CharField(max_length=11, unique=True)

    class Meta:
        # 表名
        db_table = 'tb_users'
        # 超管系统中的模块名
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        # 返回用户名,这里的用户名是AbstractUser中的
        return self.username
