# Generated by Django 4.0.4 on 2022-11-10 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jportalapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='job',
            field=models.CharField(default='nothing', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobs',
            name='workhours',
            field=models.CharField(max_length=100),
        ),
    ]