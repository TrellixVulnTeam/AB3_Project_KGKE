# Generated by Django 2.2.24 on 2021-10-18 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0002_alter_relation_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
