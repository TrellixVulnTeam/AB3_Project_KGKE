# Generated by Django 3.2.7 on 2021-09-23 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AB3_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
            ],
        ),
    ]
