# Generated by Django 4.2.3 on 2023-07-07 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating', '0003_rename_about_yourself_userprofile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.TextField(null=True),
        ),
    ]