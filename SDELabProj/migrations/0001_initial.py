# Generated by Django 4.1.3 on 2022-11-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rollno', models.BigIntegerField()),
                ('att1', models.IntegerField()),
                ('att2', models.IntegerField()),
                ('att3', models.IntegerField()),
                ('att4', models.IntegerField()),
                ('att5', models.IntegerField()),
                ('att6', models.IntegerField()),
            ],
        ),
    ]