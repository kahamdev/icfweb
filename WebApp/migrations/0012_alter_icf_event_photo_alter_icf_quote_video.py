# Generated by Django 4.0.3 on 2022-11-10 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0011_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icf_event',
            name='photo',
            field=models.FileField(blank=True, upload_to='photos/ % d/ % m/ % Y/'),
        ),
        migrations.AlterField(
            model_name='icf_quote',
            name='video',
            field=models.ImageField(blank=True, upload_to='photos/ % d/ % m/ % Y/'),
        ),
    ]
