# Generated by Django 4.1.7 on 2023-05-13 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RTO', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fine',
            name='Report_id',
        ),
        migrations.RemoveField(
            model_name='fine',
            name='User_id',
        ),
        migrations.AddField(
            model_name='fine',
            name='Fine_vehicle',
            field=models.CharField(max_length=500, null=True, verbose_name='Fine_vehicle'),
        ),
    ]
