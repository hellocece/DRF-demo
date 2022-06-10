

## 数据库

### 配置数据库

```python
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # NAME指定要连接的数据库的名称
        'NAME': 'DRFDemo',
        # USER指定登录到数据库的用户名
        'USER': 'root',
        # PASSWORD接数据库时使用的密码
        'PASSWORD': '1999331',
        # HOST连接数据库的主机
        'HOST': '127.0.0.1',
        # PORT连接数据库时使用的端口
        'PORT': '3306'
    }
}
```

### 创建数据库

```sql
create database DRFDemo default charset utf8 collate utf8_general_ci;
```

### 数据库迁移

```shell
python manage.py makemigrations
python manage.py migrate
```

### 插入测试数据

```sql
INSERT INTO `DRFDemo`.`SerializerDemo_student`(`id`, `name`, `age`, `sex`, `active`, `description`) VALUES (1, '王饱饱', 20, 0, 1, '阳光大男孩');
INSERT INTO `DRFDemo`.`SerializerDemo_student`(`id`, `name`, `age`, `sex`, `active`, `description`) VALUES (2, '董漂漂', 18, 1, 1, '阳光大男孩的女朋友');
INSERT INTO `DRFDemo`.`SerializerDemo_student`(`id`, `name`, `age`, `sex`, `active`, `description`) VALUES (3, '同学A', 20, 0, 0, '一个同学');
INSERT INTO `DRFDemo`.`SerializerDemo_teacher`(`id`, `name`, `age`, `sex`, `active`, `description`) VALUES (1, '班主任', 40, 0, 1, '我是班主任');
INSERT INTO `DRFDemo`.`ViewDemo_user`(`id`, `name`, `age`, `time_joined`) VALUES (1, '王平平', 20, '2022-06-10 08:50:33.950605');
INSERT INTO `DRFDemo`.`ViewDemo_user`(`id`, `name`, `age`, `time_joined`) VALUES (2, '董漂漂', 18, '2022-06-10 08:50:55.411997');

```


