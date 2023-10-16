from django.db import models

# Create your models here.
class Table1(models.Model):
    choice1 = [
        ('CERTIFIED-WITHDRAWN','CERTIFIED-WITHDRAWN'),
        ('WITHDRAWN','WITHDRAWN'),
        ('CERTIFIED','CERTIFIED'),
        ('DENIED','DENIED')
         ]
    choice2 = [
        ('Year', 'Year'),
        ('Bi-Weekly', 'Bi-Weekly'),
        ('Month', 'Month'),
        ('Hour', 'Hour'),
        ('Month', 'Month'),
    ]
    CASE_NUMBER = models.CharField(max_length=255, primary_key=True)
    CASE_STATUS = models.CharField(max_length=190, choices=choice1, null=True)
    CASE_SUBMITTED = models.CharField(max_length=100,null=True)
    DECISION_DATE = models.CharField(max_length=100,null=True)
    VISA_CLASS = models.CharField(max_length=140, null=True)
    EMPLOYMENT_START_DATE = models.CharField(max_length=100,null=True)
    EMPLOYMENT_END_DATE = models.CharField(max_length=100,null=True)
    EMPLOYER_NAME = models.CharField(max_length=255, null=True)
    EMPLOYER_ADDRESS = models.CharField(max_length=255,null=True)
    EMPLOYER_CITY = models.CharField(max_length=200, null=True)
    EMPLOYER_STATE = models.CharField(max_length=20, null=True)
    EMPLOYER_POSTAL_CODE = models.CharField(max_length=20, null=True)
    EMPLOYER_COUNTRY = models.CharField(max_length=500, null=True)
    EMPLOYER_PROVINCE = models.CharField(max_length=100, null=True)
    EMPLOYER_PHONE = models.CharField(max_length=130, null=True)
    EMPLOYER_PHONE_EXT = models.CharField(max_length=100, null=True)
    AGENT_ATTORNEY_NAME = models.CharField(max_length=500, null=True)
    AGENT_ATTORNEY_CITY = models.CharField(max_length=500, null=True)
    AGENT_ATTORNEY_STATE = models.CharField(max_length=20, null=True)
    JOB_TITLE = models.CharField(max_length=500,null=True)
    SOC_CODE = models.CharField(max_length=70, null=True)
    SOC_NAME = models.CharField(max_length=500, null=True)
    NAIC_CODE = models.CharField(max_length=100, null=True)
    TOTAL_WORKERS = models.CharField(max_length=400, null=True)
    FULL_TIME_POSITION = models.CharField(max_length=500,null=True)
    PREVAILING_WAGE = models.CharField(max_length=300,null=True)
    PW_UNIT_OF_PAY = models.CharField(choices=choice2, null=True)
    PW_WAGE_SOURCE = models.CharField(max_length=50, null=True)
    PW_SOURCE_OTHER = models.CharField(max_length=100,null=True)
    WAGE_RATE_OF_PAY_FROM = models.CharField(max_length=300,null=True)
    WAGE_RATE_OF_PAY_TO = models.CharField(max_length=300,null=True)
    WAGE_UNIT_OF_PAY = models.CharField(choices=choice2, null=True)
    H_1B_DEPENDENT = models.CharField(max_length=100,null=True)
    WILLFUL_VIOLATOR = models.CharField(max_length=100,blank=True)
    WORKSITE_CITY = models.CharField(max_length=500,null=True)
    WORKSITE_COUNTY = models.CharField(max_length=500,null=True)
    WORKSITE_STATE = models.CharField(max_length=500,null=True)
    WORKSITE_POSTAL_CODE = models.CharField(max_length=500,blank=True)
    ORIGINAL_CERT_DATE = models.CharField(max_length=200,null=True)

