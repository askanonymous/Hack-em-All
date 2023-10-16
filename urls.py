from django.contrib import admin
from django.urls import path
from Home import views
# from views import CompanyViewSet
# from rest_framework import routers

# router=routers.DefaultRouter()
# router.register(r'companies',CompanyViewSet)

urlpatterns = [
    path("",views.home,name="home"),
    path("contact",views.contact,name="contact"),
    path("data",views.datareport,name="report")
]
