from django.shortcuts import render
import csv
from .models import Table1
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from rest_framework import viewsets
# from Home.models import Company
# from Home.serializers import CompanySerializer

# Create your views here.

# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class=CompanySerializer

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'Contact.html')

def datareport(request):
    return render(request,'datareport.html')


# views.py

def import_csv(request):
    if request.method == "POST" and request.FILES.get('DataAnalysis\static\H-1B_Disclosure_Data_FY16.csv'):
        csv_file = request.FILES['DataAnalysis\static\H-1B_Disclosure_Data_FY16.csv']
        data = csv.reader(csv_file)
        
        for row in data:
            case_number, case_status, case_submitted, decision_date, visa_class, employment_start_date, employment_end_date, employer_name, employer_address, employer_city, employer_state, employer_postal_code, employer_country, employer_province, employer_phone, emploter_phone_ext, agent_attorney_name, agent_attorney_city, agent_attorney_state, job_title, soc_code, soc_name, naic_code, total_workers, fulltime_position, prevailing_wage, pw_unit_of_pay, pw_wage_source, pw_source_other, wage_rate_of_pay_from, wage_rate_of_pay_to, wage_unit_of_pay, h_1b_dependent, wilful_violator, worksite_city, worksite_county, worksite_state, worksite_postal_code, original_cert_data = row
            
            # Create and save a new instance of Table1 with the data from the CSV
            table1_instance = Table1(
                case_number=case_number, case_status=case_status, case_submitted=case_submitted,
                decision_date=decision_date, visa_class=visa_class, employment_start_date=employment_start_date,
                employment_end_date=employment_end_date, employer_name=employer_name, employer_address=employer_address,
                employer_city=employer_city, employer_state=employer_state, employer_postal_code=employer_postal_code,
                employer_country=employer_country, employer_province=employer_province, employer_phone=employer_phone,
                emploter_phone_ext=emploter_phone_ext, agent_attorney_name=agent_attorney_name,
                agent_attorney_city=agent_attorney_city, agent_attorney_state=agent_attorney_state, job_title=job_title,
                soc_code=soc_code, soc_name=soc_name, naic_code=naic_code, total_workers=total_workers,
                fulltime_position=fulltime_position, prevailing_wage=prevailing_wage, pw_unit_of_pay=pw_unit_of_pay,
                pw_wage_source=pw_wage_source, pw_source_other=pw_source_other, wage_rate_of_pay_from=wage_rate_of_pay_from,
                wage_rate_of_pay_to=wage_rate_of_pay_to, wage_unit_of_pay=wage_unit_of_pay,
                h_1b_dependent=h_1b_dependent, wilful_violator=wilful_violator, worksite_city=worksite_city,
                worksite_county=worksite_county, worksite_state=worksite_state, worksite_postal_code=worksite_postal_code,
                original_cert_data=original_cert_data
            )
            table1_instance.save()
        
        return HttpResponse("Successfully stored data")  # Redirect to a success page

    return render(request, 'import_csv.html')  # Render the form