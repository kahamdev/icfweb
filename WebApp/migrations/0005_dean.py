# Generated by Django 3.2.8 on 2021-10-26 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0004_auto_20211023_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dean',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
