# Generated by Django 2.1.3 on 2018-11-11 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(default='#', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default='Project', max_length=20),
        ),
    ]