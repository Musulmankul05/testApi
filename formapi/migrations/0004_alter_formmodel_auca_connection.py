# Generated by Django 5.0.2 on 2024-02-26 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapi', '0003_rename_kgs_formmodel_som'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formmodel',
            name='auca_connection',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
