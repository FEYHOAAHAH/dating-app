# Generated by Django 4.2.2 on 2023-06-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('status', models.CharField(choices=[('st', 'Учусь'), ('wk', 'Работаю'), ('sd', 'Туплю'), ('md', 'Мамкин миллиардер'), ('rf', 'АААА')], max_length=50)),
                ('about_yourself', models.TextField()),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
