# Generated by Django 4.2.6 on 2023-10-25 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('surname', models.CharField(max_length=100, null=True)),
                ('fatherName', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='BlackList',
        ),
        migrations.AddField(
            model_name='phones',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.users'),
        ),
    ]
