# Generated by Django 3.2.8 on 2021-10-27 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0006_auto_20211027_0051'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmiratDawaLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amirat_dawa_name', models.CharField(max_length=100)),
                ('amirat_dawa_regno', models.CharField(max_length=100)),
                ('amirat_dawa_program', models.CharField(max_length=100)),
                ('amirat_dawa_year', models.IntegerField()),
                ('amirat_dawa_status', models.CharField(max_length=100)),
                ('amirat_dawa_mobile', models.CharField(max_length=100)),
                ('naibu_amirat_dawa_name', models.CharField(max_length=100)),
                ('naibu_amirat_dawa_regno', models.CharField(max_length=100)),
                ('naibu_amirat_dawa_program', models.CharField(max_length=100)),
                ('naibu_amirat_dawa_year', models.IntegerField()),
                ('naibu_amirat_dawa_status', models.CharField(max_length=100)),
                ('naibu_amirat_dawa_mobile', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AmiratFedhaLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amirat_fedha_name', models.CharField(max_length=100)),
                ('amirat_fedha_regno', models.CharField(max_length=100)),
                ('amirat_fedha_program', models.CharField(max_length=100)),
                ('amirat_fedha_year', models.IntegerField()),
                ('amirat_fedha_status', models.CharField(max_length=100)),
                ('amirat_fedha_mobile', models.CharField(max_length=100)),
                ('naibu_amirat_fedha_name', models.CharField(max_length=100)),
                ('naibu_amirat_fedha_regno', models.CharField(max_length=100)),
                ('naibu_amirat_fedha_program', models.CharField(max_length=100)),
                ('naibu_amirat_fedha_year', models.IntegerField()),
                ('naibu_amirat_fedha_status', models.CharField(max_length=100)),
                ('naibu_amirat_fedha_mobile', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AmiratHabarLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amirat_habar_name', models.CharField(max_length=100)),
                ('amirat_habar_regno', models.CharField(max_length=100)),
                ('amirat_habar_program', models.CharField(max_length=100)),
                ('amirat_habar_year', models.IntegerField()),
                ('amirat_fedha_status', models.CharField(max_length=100)),
                ('amirat_habar_mobile', models.CharField(max_length=100)),
                ('naibu_amirat_habar_name', models.CharField(max_length=100)),
                ('naibu_amirat_habar_regno', models.CharField(max_length=100)),
                ('naibu_amirat_habar_program', models.CharField(max_length=100)),
                ('naibu_amirat_habar_year', models.IntegerField()),
                ('naibu_amirat_habar_status', models.CharField(max_length=100)),
                ('naibu_amirat_habar_mobile', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AmirDawaLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amir_dawa_name', models.CharField(max_length=100)),
                ('amir_dawa_regno', models.CharField(max_length=100)),
                ('amir_dawa_program', models.CharField(max_length=100)),
                ('amir_dawa_year', models.IntegerField()),
                ('amir_dawa_status', models.CharField(max_length=100)),
                ('amir_dawa_mobile', models.CharField(max_length=100)),
                ('naibu_amir_dawa_name', models.CharField(max_length=100)),
                ('naibu_amir_dawa_regno', models.CharField(max_length=100)),
                ('naibu_amir_dawa_program', models.CharField(max_length=100)),
                ('naibu_amir_dawa_year', models.IntegerField()),
                ('naibu_amir_dawa_status', models.CharField(max_length=100)),
                ('naibu_amir_dawa_mobile', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AmirFedhaLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amir_fedha_name', models.CharField(max_length=100)),
                ('amir_fedha_regno', models.CharField(max_length=100)),
                ('amir_fedha_program', models.CharField(max_length=100)),
                ('amir_fedha_year', models.IntegerField()),
                ('amir_fedha_status', models.CharField(max_length=100)),
                ('amir_fedha_mobile', models.CharField(max_length=100)),
                ('naibu_amir_fedha_name', models.CharField(max_length=100)),
                ('naibu_amir_fedha_regno', models.CharField(max_length=100)),
                ('naibu_amir_fedha_program', models.CharField(max_length=100)),
                ('naibu_amir_fedha_year', models.IntegerField()),
                ('naibu_amir_fedha_status', models.CharField(max_length=100)),
                ('naibu_amir_fedha_mobile', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AmirHabarLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amir_habar_name', models.CharField(max_length=100)),
                ('amir_habar_regno', models.CharField(max_length=100)),
                ('amir_habar_program', models.CharField(max_length=100)),
                ('amir_habar_year', models.IntegerField()),
                ('amir_fedha_status', models.CharField(max_length=100)),
                ('amir_habar_mobile', models.CharField(max_length=100)),
                ('naibu_amir_habar_name', models.CharField(max_length=100)),
                ('naibu_amir_habar_regno', models.CharField(max_length=100)),
                ('naibu_amir_habar_program', models.CharField(max_length=100)),
                ('naibu_amir_habar_year', models.IntegerField()),
                ('naibu_amir_habar_status', models.CharField(max_length=100)),
                ('naibu_amir_habar_mobile', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ImamsLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('imamu1_name', models.CharField(max_length=100)),
                ('imamu1_regno', models.CharField(max_length=100)),
                ('imamu1_program', models.CharField(max_length=100)),
                ('imamu1_year', models.IntegerField()),
                ('imamu1_status', models.CharField(max_length=100)),
                ('imamu1_mobile', models.CharField(max_length=100)),
                ('imamu2_name', models.CharField(max_length=100)),
                ('imamu2_regno', models.CharField(max_length=100)),
                ('imamu2_program', models.CharField(max_length=100)),
                ('imamu2_year', models.IntegerField()),
                ('imamu2_status', models.CharField(max_length=100)),
                ('imamu2_mobile', models.CharField(max_length=100)),
                ('imamu3_name', models.CharField(max_length=100)),
                ('imamu3_regno', models.CharField(max_length=100)),
                ('imamu3_program', models.CharField(max_length=100)),
                ('imamu3_year', models.IntegerField()),
                ('imamu3_status', models.CharField(max_length=100)),
                ('imamu3_mobile', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MudiratLeader',
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
            name='MudirLeader',
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
        migrations.RenameModel(
            old_name='FemaleLeaders',
            new_name='KatibatLeader',
        ),
        migrations.RenameModel(
            old_name='MaleLeaders',
            new_name='KatibuLeader',
        ),
        migrations.RenameField(
            model_name='katibatleader',
            old_name='mudirat_mobile',
            new_name='katibat_mobile',
        ),
        migrations.RenameField(
            model_name='katibatleader',
            old_name='mudirat_name',
            new_name='katibat_name',
        ),
        migrations.RenameField(
            model_name='katibatleader',
            old_name='mudirat_program',
            new_name='katibat_program',
        ),
        migrations.RenameField(
            model_name='katibatleader',
            old_name='mudirat_regno',
            new_name='katibat_regno',
        ),
        migrations.RenameField(
            model_name='katibatleader',
            old_name='naibu_mudirat_mobile',
            new_name='katibat_status',
        ),
        migrations.RenameField(
            model_name='katibatleader',
            old_name='mudirat_year',
            new_name='katibat_year',
        ),
        migrations.RenameField(
            model_name='katibatleader',
            old_name='mudirat_status',
            new_name='naibu_katibat_mobile',
        ),
        migrations.RenameField(
            model_name='katibatleader',
            old_name='naibu_mudirat_name',
            new_name='naibu_katibat_name',
        ),
        migrations.RenameField(
            model_name='katibatleader',
            old_name='naibu_mudirat_program',
            new_name='naibu_katibat_program',
        ),
        migrations.RenameField(
            model_name='katibatleader',
            old_name='naibu_mudirat_regno',
            new_name='naibu_katibat_regno',
        ),
        migrations.RenameField(
            model_name='katibatleader',
            old_name='naibu_mudirat_status',
            new_name='naibu_katibat_status',
        ),
        migrations.RenameField(
            model_name='katibuleader',
            old_name='mudir_mobile',
            new_name='katibu_mobile',
        ),
        migrations.RenameField(
            model_name='katibuleader',
            old_name='mudir_name',
            new_name='katibu_name',
        ),
        migrations.RenameField(
            model_name='katibuleader',
            old_name='mudir_program',
            new_name='katibu_program',
        ),
        migrations.RenameField(
            model_name='katibuleader',
            old_name='mudir_regno',
            new_name='katibu_regno',
        ),
        migrations.RenameField(
            model_name='katibuleader',
            old_name='mudir_status',
            new_name='katibu_status',
        ),
        migrations.RenameField(
            model_name='katibuleader',
            old_name='mudir_year',
            new_name='katibu_year',
        ),
        migrations.RenameField(
            model_name='katibuleader',
            old_name='naibu_mudir_mobile',
            new_name='naibu_katibu_mobile',
        ),
        migrations.RenameField(
            model_name='katibuleader',
            old_name='naibu_mudir_name',
            new_name='naibu_katibu_name',
        ),
        migrations.RenameField(
            model_name='katibuleader',
            old_name='naibu_mudir_program',
            new_name='naibu_katibu_program',
        ),
        migrations.RenameField(
            model_name='katibuleader',
            old_name='naibu_mudir_regno',
            new_name='naibu_katibu_regno',
        ),
        migrations.RenameField(
            model_name='katibuleader',
            old_name='naibu_mudir_status',
            new_name='naibu_katibu_status',
        ),
        migrations.RenameField(
            model_name='katibuleader',
            old_name='naibu_mudir_year',
            new_name='naibu_katibu_year',
        ),
        migrations.RemoveField(
            model_name='katibatleader',
            name='naibu_mudirat_year',
        ),
        migrations.AddField(
            model_name='katibatleader',
            name='naibu_katibat_year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]