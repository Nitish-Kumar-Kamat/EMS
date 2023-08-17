from django.urls import path
from .import views

urlpatterns=[
  path('',views.userClick, name="userClick"),
  path('userReg/',views.userReg, name="userReg"),
  path('userLogin/',views.userLogin, name="userLogin"),
  path('uregistration/',views.uregistration, name="uregistration"),
  path('ulogin/',views.ulogin, name="ulogin"),
  path('uafterlogin/',views.uafterlogin, name="uafterlogin"),
  path('uenquiryform/',views.uenquiryform, name='uenquiryform'),
  path('uenquiryTask/',views.uenquiryTask, name='uenquiryTask'),
  path('DisplayAdmin/',views.DisplayAdmin,name="DisplayAdmin"),
  path('delete/<int:id>/',views.deletedata, name="deletedata"),
  path('update/<int:id>/',views.updatedata,name="updatedata"),
  # path('myenqu/',views.myenq, name="myenq"),
 
]