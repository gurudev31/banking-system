# Generated by Django 5.0.4 on 2024-06-26 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_delete_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='connection',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='info',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='notification',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='social',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]