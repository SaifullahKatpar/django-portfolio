# Generated by Django 2.1.3 on 2018-11-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20181112_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(default='Project', max_length=40),
        ),
    ]
