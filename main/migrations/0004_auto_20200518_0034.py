# Generated by Django 3.0.5 on 2020-05-17 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200517_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='mehfildetail',
            name='sadaratimag',
            field=models.ImageField(default='', upload_to='main/slider'),
        ),
        migrations.AlterField(
            model_name='mehfildetail',
            name='sadarat',
            field=models.CharField(max_length=50),
        ),
    ]