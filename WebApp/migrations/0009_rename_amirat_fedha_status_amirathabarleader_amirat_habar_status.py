# Generated by Django 3.2.8 on 2021-10-28 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0008_rename_amir_fedha_status_amirhabarleader_amir_habar_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amirathabarleader',
            old_name='amirat_fedha_status',
            new_name='amirat_habar_status',
        ),
    ]
