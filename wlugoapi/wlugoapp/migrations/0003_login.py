# Generated by Django 2.2.5 on 2021-08-01 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wlugoapp', '0002_auto_20210729_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('email', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='email')),
                ('first_name', models.CharField(max_length=20, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=20, verbose_name='last_name')),
                ('password', models.CharField(max_length=20, verbose_name='password')),
                ('leave', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wlugoapp.User')),
            ],
        ),
    ]
