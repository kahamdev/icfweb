# Generated by Django 4.0.3 on 2022-11-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0012_alter_icf_event_photo_alter_icf_quote_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='icf_quote',
            old_name='video',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='icf_event',
            name='photo',
        ),
        migrations.AddField(
            model_name='icf_event',
            name='video',
            field=models.FileField(blank=True, upload_to='video/ % d/ % m/ % Y/'),
        ),
    ]
