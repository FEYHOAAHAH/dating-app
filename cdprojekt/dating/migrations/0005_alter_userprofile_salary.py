# Generated by Django 4.2.3 on 2023-07-07 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating', '0004_alter_userprofile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='salary',
            field=models.IntegerField(null=True),
        ),
    ]
