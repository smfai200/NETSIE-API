# Generated by Django 2.2.9 on 2020-01-27 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200127_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='IsActive',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
