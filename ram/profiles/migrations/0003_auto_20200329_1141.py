# Generated by Django 3.0.3 on 2020-03-29 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20200329_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='email',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='email',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='ta',
            old_name='email',
            new_name='user',
        ),
    ]
