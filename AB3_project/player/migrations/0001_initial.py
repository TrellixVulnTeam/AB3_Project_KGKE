# Generated by Django 3.2.7 on 2021-09-30 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('state', models.CharField(choices=[('AV', 'Avaiable'), ('DB', 'Doubtful'), ('RO', 'Ruled Out')], default='AV', max_length=100)),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='players', to='team.team')),
            ],
        ),
    ]
