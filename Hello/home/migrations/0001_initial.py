# Generated by Django 4.1.5 on 2023-01-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=80)),
                ('issue', models.TextField()),
            ],
        ),
    ]
