# Generated by Django 4.2.6 on 2023-10-25 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_users_about_users_age_users_idnumber_users_iscar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='age',
        ),
        migrations.AddField(
            model_name='users',
            name='birthday',
            field=models.CharField(max_length=100, null=True),
        ),
    ]