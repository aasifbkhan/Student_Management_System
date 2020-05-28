# Generated by Django 3.0.6 on 2020-05-20 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('roll_no', models.CharField(max_length=10)),
                ('DOB', models.DateField()),
                ('course', models.CharField(max_length=20)),
                ('admit_year', models.IntegerField(max_length=4)),
                ('gender', models.CharField(max_length=6)),
                ('contact', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('state', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=15)),
                ('zip_code', models.IntegerField(max_length=6)),
                ('fees', models.FloatField()),
            ],
        ),
    ]