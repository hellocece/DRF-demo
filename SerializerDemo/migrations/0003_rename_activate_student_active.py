# Generated by Django 4.0.4 on 2022-06-09 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SerializerDemo', '0002_alter_student_activate_alter_student_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='activate',
            new_name='active',
        ),
    ]