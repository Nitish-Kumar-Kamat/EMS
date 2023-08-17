from django.urls import path
from .import views

urlpatterns=[
  path('',views.adminClick, name='adminClick'),
  path('adminReg/',views.adminReg, name='adminReg'),
  path('adminLogin/',views.adminLogin, name='adminLogin'),
  path('aregistration/',views.aregistration,name='aregistration'),
  path('alogin/',views.alogin, name='alogin'),
  path('aAfterlogin/',views.aAfterlogin, name='aAfterlogin'),
]