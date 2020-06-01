# Generated by Django 3.0.5 on 2020-05-31 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email Address')),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contacter', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mehfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='postrequest',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('address', models.CharField(default='', max_length=70)),
                ('attendences', models.CharField(default='', max_length=50)),
                ('date', models.DateField(default='', max_length=70)),
                ('time', models.TimeField(default='', max_length=70)),
                ('poster', models.ImageField(default='', upload_to='main/slider')),
                ('desc', models.CharField(max_length=300)),
                ('verification', models.BooleanField(default=False)),
                ('phone_no', models.CharField(default='', max_length=10)),
                ('organiser', models.CharField(default='', max_length=50)),
                ('taam', models.BooleanField(default=False)),
                ('category', models.CharField(choices=[('mehfil', 'Mehfil'), ('majlis', 'Majlis'), ('others', 'Others')], default='others', max_length=50)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.city')),
            ],
        ),
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_image', models.ImageField(upload_to='main/slider')),
            ],
        ),
        migrations.CreateModel(
            name='Shaiyar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shaiyarname', models.CharField(max_length=50)),
                ('photo', models.ImageField(default='', upload_to='main/slider')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.postrequest')),
            ],
        ),
        migrations.CreateModel(
            name='mehfildetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nizamat', models.CharField(max_length=50)),
                ('nizamimage', models.ImageField(default='', upload_to='main/slider')),
                ('sadarat', models.CharField(max_length=50)),
                ('sadaratimag', models.ImageField(default='', upload_to='main/slider')),
                ('mehfil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.postrequest')),
            ],
        ),
    ]
