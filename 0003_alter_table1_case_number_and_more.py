# Generated by Django 4.2.6 on 2023-10-15 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_rename_case_number_table1_case_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table1',
            name='CASE_NUMBER',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='table1',
            name='EMPLOYER_ADDRESS',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
