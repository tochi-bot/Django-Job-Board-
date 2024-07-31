# Generated by Django 4.2.14 on 2024-07-31 11:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0002_alter_employerprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employerprofile',
            old_name='company_description',
            new_name='description',
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='website',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='company_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
