# Generated by Django 4.2.6 on 2023-11-04 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_users_userid_alter_cards_userid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='friendId',
            field=models.IntegerField(null=True),
        ),
    ]
