# Generated by Django 2.2.3 on 2019-08-07 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomStrategy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomBacktest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '回测',
                'verbose_name_plural': '回测',
            },
        ),
    ]
