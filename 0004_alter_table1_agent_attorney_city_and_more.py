# Generated by Django 4.2.6 on 2023-10-15 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_table1_case_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table1',
            name='AGENT_ATTORNEY_CITY',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='AGENT_ATTORNEY_NAME',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='EMPLOYER_COUNTRY',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='FULL_TIME_POSITION',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='JOB_TITLE',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='WORKSITE_CITY',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='WORKSITE_COUNTY',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='table1',
            name='WORKSITE_POSTAL_CODE',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='table1',
            name='WORKSITE_STATE',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
