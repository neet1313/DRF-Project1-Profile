# Generated by Django 4.2 on 2023-05-06 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles_API', '0002_auto_20230426_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
