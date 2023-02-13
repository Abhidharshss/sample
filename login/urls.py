from.import views
from django.urls import path

urlpatterns =[
    path("",views.login,name=""),
    path("login",views.login,name="login"),
    path("adminhome",views.adminhome,name="adminhome"),
    path("userreg",views.userreg,name="userreg"),
    path("logi",views.logi,name="logi"),
    path("delusr",views.delusr,name="delusr"),
    path("sample",views.sample,name="sample"),
    path("editusr",views.editusr,name="editusr"),
    path("logoutfrom",views.logoutfrom,name="logoutfrom"),
]