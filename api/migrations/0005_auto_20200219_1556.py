# Generated by Django 2.2.9 on 2020-02-19 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200127_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='UserProfile_User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UserFavourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Story', models.CharField(blank=True, max_length=250, null=True)),
                ('Season', models.FileField(blank=True, null=True, upload_to='static/uploads/')),
                ('Episode', models.CharField(blank=True, max_length=250, null=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('CreateDate', models.DateTimeField(auto_now_add=True)),
                ('UpdateDate', models.DateTimeField(auto_now=True)),
                ('User_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='api.UserProfile')),
            ],
            options={
                'verbose_name_plural': 'UserFavourites',
            },
        ),
    ]