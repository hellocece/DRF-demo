

## 数据库

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
```


