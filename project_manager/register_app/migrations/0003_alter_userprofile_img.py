# Generated by Django 4.1.5 on 2023-02-01 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_app', '0002_delete_normaluser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(blank=True, default='img/avatar/blank_profile.png', upload_to='profile'),
        ),
    ]
