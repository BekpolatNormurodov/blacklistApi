# Generated by Django 4.2.6 on 2023-12-04 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_remove_users_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
