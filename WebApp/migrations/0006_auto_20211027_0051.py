# Generated by Django 3.2.8 on 2021-10-27 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0005_dean'),
    ]

    operations = [
        migrations.CreateModel(
            name='FemaleLeaders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('mudirat_name', models.CharField(max_length=100)),
                ('naibu_mudirat_name', models.CharField(max_length=100)),
                ('mudirat_regno', models.CharField(max_length=100)),
                ('naibu_mudirat_regno', models.CharField(max_length=100)),
                ('mudirat_program', models.CharField(max_length=100)),
                ('naibu_mudirat_program', models.CharField(max_length=100)),
                ('mudirat_status', models.CharField(max_length=100)),
                ('naibu_mudirat_status', models.CharField(max_length=100)),
                ('mudirat_mobile', models.CharField(max_length=100)),
                ('naibu_mudirat_mobile', models.CharField(max_length=100)),
                ('mudirat_year', models.IntegerField()),
                ('naibu_mudirat_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MaleLeaders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('mudir_name', models.CharField(max_length=100)),
                ('naibu_mudir_name', models.CharField(max_length=100)),
                ('mudir_regno', models.CharField(max_length=100)),
                ('naibu_mudir_regno', models.CharField(max_length=100)),
                ('mudir_program', models.CharField(max_length=100)),
                ('naibu_mudir_program', models.CharField(max_length=100)),
                ('mudir_status', models.CharField(max_length=100)),
                ('naibu_mudir_status', models.CharField(max_length=100)),
                ('mudir_mobile', models.CharField(max_length=100)),
                ('naibu_mudir_mobile', models.CharField(max_length=100)),
                ('mudir_year', models.IntegerField()),
                ('naibu_mudir_year', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Leaders',
        ),
        migrations.AlterField(
            model_name='dean',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]