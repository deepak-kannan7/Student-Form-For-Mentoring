# Generated by Django 4.1.1 on 2022-12-12 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SDELabProj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark1', models.IntegerField()),
                ('mark2', models.IntegerField()),
                ('mark3', models.IntegerField()),
                ('mark4', models.IntegerField()),
                ('mark5', models.IntegerField()),
                ('mark6', models.IntegerField()),
            ],
        ),
    ]
