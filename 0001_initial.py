# Generated by Django 4.2.6 on 2023-10-15 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table1',
            fields=[
                ('case_number', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('case_status', models.CharField(blank=True, choices=[('CERTIFIED-WITHDRAWN', 'CERTIFIED-WITHDRAWN'), ('WITHDRAWN', 'WITHDRAWN'), ('CERTIFIED', 'CERTIFIED'), ('DENIED', 'DENIED')], max_length=19)),
                ('case_submitted', models.DateField(blank=True)),
                ('decision_date', models.DateField(blank=True)),
                ('visa_class', models.CharField(blank=True, max_length=14)),
                ('employment_start_date', models.DateField(blank=True)),
                ('employment_end_date', models.DateField(blank=True)),
                ('employer_name', models.CharField(blank=True, max_length=255)),
                ('employer_address', models.TextField(blank=True)),
                ('employer_city', models.CharField(blank=True, max_length=20)),
                ('employer_state', models.CharField(blank=True, max_length=2)),
                ('employer_postal_code', models.IntegerField(blank=True, max_length=20)),
                ('employer_country', models.CharField(blank=True, max_length=50)),
                ('employer_province', models.CharField(blank=True, max_length=100)),
                ('employer_phone', models.IntegerField(blank=True, max_length=13)),
                ('emploter_phone_ext', models.CharField(blank=True, max_length=10)),
                ('agent_attorney_name', models.CharField(blank=True, max_length=50)),
                ('agent_attorney_city', models.CharField(blank=True, max_length=50)),
                ('agent_attorney_state', models.CharField(blank=True, max_length=2)),
                ('job_title', models.TextField(blank=True)),
                ('soc_code', models.CharField(blank=True, max_length=7)),
                ('soc_name', models.CharField(blank=True, max_length=50)),
                ('naic_code', models.IntegerField(blank=True, max_length=10)),
                ('total_workers', models.IntegerField(blank=True, max_length=4)),
                ('fulltime_position', models.CharField(null=True)),
                ('prevailing_wage', models.FloatField()),
                ('pw_unit_of_pay', models.CharField(choices=[('Year', 'Year'), ('Bi-Weekly', 'Bi-Weekly'), ('Month', 'Month'), ('Hour', 'Hour'), ('Month', 'Month')])),
                ('pw_wage_source', models.CharField(blank=True, max_length=5)),
                ('pw_source_other', models.CharField(blank=True, max_length=100)),
                ('wage_rate_of_pay_from', models.FloatField()),
                ('wage_rate_of_pay_to', models.FloatField()),
                ('wage_unit_of_pay', models.CharField(choices=[('Year', 'Year'), ('Bi-Weekly', 'Bi-Weekly'), ('Month', 'Month'), ('Hour', 'Hour'), ('Month', 'Month')])),
                ('h_1b_dependent', models.CharField(blank=True, max_length=10)),
                ('wilful_voilator', models.CharField(blank=True, max_length=10)),
                ('worksite_city', models.CharField(blank=True, max_length=50)),
                ('worksite_county', models.CharField(blank=True, max_length=50)),
                ('worksite_state', models.CharField(blank=True, max_length=50)),
                ('worksite_postal_code', models.CharField(blank=True, max_length=50)),
                ('original_cert_data', models.DateField(blank=True)),
            ],
        ),
    ]