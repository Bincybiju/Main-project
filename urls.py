
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('AdminHome',views.AdminHome,name="AdminHome"),
    path('UserHome',views.UserHome,name="UserHome"),
    path('StaffHome',views.StaffHome,name="StaffHome"),
    path('Login',views.Login,name="Login"),
    path('Privacy',views.Privacy,name="Privacy"),
    path('Logout',views.Logout,name="Logout"),
    path('Appoint_Staff',views.Appoint_Staff,name="Appoint_Staff"),
    path('Our_Staff',views.Our_Staff,name="Our_Staff"),
    path('delete_staff',views.delete_staff,name="delete_staff"),
    path('Our_Users',views.Our_Users,name="Our_Users"),
    path('Current_Users',views.Current_Users,name="Current_Users"),
    path('delete_user',views.delete_user,name="delete_user"),
    path('delete_user1',views.delete_user1,name="delete_user1"),
    path('Register_vehicle',views.Register_vehicle,name="Register_vehicle"),
    path('Manage_complaints',views.Manage_complaints,name="Manage_complaints"),
    path('my_reports',views.my_reports,name="my_reports"),
    path('my_Payemnts',views.my_Payemnts,name="my_Payemnts"),
    path('complaints',views.complaints,name="complaints"),
    path('fine_pay',views.fine_pay,name="fine_pay"),
    path('reports',views.reports,name="reports"),
    path('fine_report',views.fine_report,name="fine_report"),
    path('alert',views.alert,name="alert"),
    path('pay',views.pays,name="pay"),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
