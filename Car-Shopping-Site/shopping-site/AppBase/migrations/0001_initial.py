# Generated by Django 3.0.3 on 2021-06-01 06:33

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppDefaultIocn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='名称')),
                ('img', models.ImageField(default='userimage/qq.jpg', upload_to='defaultIocn', verbose_name='头像')),
            ],
            options={
                'verbose_name': '默认图标字典',
                'verbose_name_plural': '默认图标字典',
            },
        ),
        migrations.CreateModel(
            name='AppMenuDict',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, default='', max_length=128, verbose_name='菜单编码')),
                ('name', models.CharField(max_length=128, verbose_name='菜单名称')),
                ('parent_id', models.IntegerField(default=0, verbose_name='父级菜单id')),
                ('url', models.CharField(blank=True, default='', max_length=128, verbose_name='菜单路由')),
                ('disabled_flag', models.IntegerField(default=0, verbose_name='不可用标识')),
                ('order_num', models.IntegerField(default=0, verbose_name='排序号')),
                ('icon', models.CharField(blank=True, max_length=128, verbose_name='菜单fa图标')),
                ('description', models.CharField(blank=True, max_length=128, verbose_name='菜单描述')),
            ],
            options={
                'verbose_name': '菜单字典',
                'verbose_name_plural': '菜单字典',
            },
        ),
        migrations.CreateModel(
            name='AppSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=128, verbose_name='配置项名')),
                ('value', models.CharField(max_length=128, verbose_name='值')),
                ('description', models.CharField(max_length=128, verbose_name='配置描述')),
            ],
            options={
                'verbose_name': '系统配置',
                'verbose_name_plural': '系统配置',
            },
        ),
        migrations.CreateModel(
            name='EmailSendFromDefaultSettings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('smtpServer', models.CharField(default='', max_length=256, verbose_name='使用的SMTP服务')),
                ('formUser', models.CharField(default='', max_length=256, verbose_name='发件人')),
                ('userPassword', models.CharField(default='', max_length=256, verbose_name='发件人邮件授权登录密码')),
                ('userShowName', models.CharField(default='', max_length=256, verbose_name='发送邮件显示发件人别名')),
            ],
            options={
                'verbose_name': '邮箱设置',
                'verbose_name_plural': '邮箱设置',
            },
        ),
        migrations.CreateModel(
            name='UserDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=32, verbose_name='手机号码')),
                ('role', models.CharField(default='', max_length=32, verbose_name='用户角色')),
                ('lvl', models.IntegerField(default=1, verbose_name='用户等级')),
                ('img', models.ImageField(default='userimage/qq.jpg', upload_to='userimage', verbose_name='用户头像')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户字典',
                'verbose_name_plural': '用户字典',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
