import csv
import os
import django


# Configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DataAnalysis.settings")
django.setup()

from django.conf import settings
from Home.models import Table1

# Define the path to your CSV file
csv_file_path = "D:\STGI Hackathon\DataAnalysis\static\H-1B_Disclosure_Data_FY16.csv"  # Replace with your CSV file path

# Read and import data from the CSV file
with open(csv_file_path, 'r') as file:
    csv_data = csv.DictReader(file)
    next(csv_data)

    for row in csv_data:
        # Create an instance of Table1 and populate fields from the CSV
        
        table1_instance = Table1(
            CASE_NUMBER=row['ï»¿CASE_NUMBER'],
            CASE_STATUS=row['CASE_STATUS'],
            CASE_SUBMITTED=row['CASE_SUBMITTED'],
            DECISION_DATE=row['DECISION_DATE'],
            VISA_CLASS=row['VISA_CLASS'],
            EMPLOYMENT_START_DATE=row['EMPLOYMENT_START_DATE'],
            EMPLOYMENT_END_DATE=row['EMPLOYMENT_END_DATE'],
            EMPLOYER_NAME=row['EMPLOYER_NAME'],
            EMPLOYER_ADDRESS=row['EMPLOYER_ADDRESS'],
            EMPLOYER_CITY=row['EMPLOYER_CITY'],
            EMPLOYER_STATE=row['EMPLOYER_STATE'],
            EMPLOYER_POSTAL_CODE=row['EMPLOYER_POSTAL_CODE'],
            EMPLOYER_COUNTRY=row['EMPLOYER_COUNTRY'],
            EMPLOYER_PROVINCE=row['EMPLOYER_PROVINCE'],
            EMPLOYER_PHONE=row['EMPLOYER_PHONE'],
            EMPLOYER_PHONE_EXT=row['EMPLOYER_PHONE_EXT'],
            AGENT_ATTORNEY_NAME=row['AGENT_ATTORNEY_NAME'],
            AGENT_ATTORNEY_CITY=row['AGENT_ATTORNEY_CITY'],
            AGENT_ATTORNEY_STATE=row['AGENT_ATTORNEY_STATE'],
            JOB_TITLE=row['JOB_TITLE'],
            SOC_CODE=row['SOC_CODE'],
            SOC_NAME=row['SOC_NAME'],
            NAIC_CODE=row['NAIC_CODE'],
            TOTAL_WORKERS=row['TOTAL_WORKERS'],
            FULL_TIME_POSITION=row['FULL_TIME_POSITION'],
            PREVAILING_WAGE=row['PREVAILING_WAGE'],
            PW_UNIT_OF_PAY=row['PW_UNIT_OF_PAY'],
            PW_WAGE_SOURCE=row['PW_WAGE_SOURCE'],
            PW_SOURCE_OTHER=row['PW_SOURCE_OTHER'],
            WAGE_RATE_OF_PAY_FROM=row['WAGE_RATE_OF_PAY_FROM'],
            WAGE_RATE_OF_PAY_TO=row['WAGE_RATE_OF_PAY_TO'],
            WAGE_UNIT_OF_PAY=row['WAGE_UNIT_OF_PAY'],
            H_1B_DEPENDENT=row['H-1B_DEPENDENT'],
            WILLFUL_VIOLATOR=row['WILLFUL_VIOLATOR'],
            WORKSITE_CITY=row['WORKSITE_CITY'],
            WORKSITE_COUNTY=row['WORKSITE_COUNTY'],
            WORKSITE_STATE=row['WORKSITE_STATE'],
            WORKSITE_POSTAL_CODE=row['WORKSITE_POSTAL_CODE'],
            ORIGINAL_CERT_DATE=row['ORIGINAL_CERT_DATE']
        )

        
        table1_instance.save()

print("Data imported successfully.")