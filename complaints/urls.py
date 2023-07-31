from django.urls import path
from complaints.views import About,Home,Contact,Login,Logout_admin,Useri,regcomplaints,Viewstatcomplaints,Feedcomplaints,Staffdash,Viewcomplaints,Logout_user,Index,Login_govt, Adduser
from .import views 



urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('admin_login/', Login, name='admin_login'),
    path('logout_admin/', Logout_admin, name='logout_admin'),
    path('index/', Index, name='index'),
    path('adduser/', Adduser, name='adduser'),
    path('useri/', Useri, name='useri'),
    path('regcomplaints/', regcomplaints, name='regcomplaints'),
    path('viewstatcomplaints/', Viewstatcomplaints, name='viewstatcomplaints'),
    path('feedcomplaints/', Feedcomplaints, name='feedcomplaints'),
    path('staffdash/', Staffdash, name='staffdash'),
    path('viewcomplaints/', Viewcomplaints, name='viewcomplaints'),
    path('user/signup/',views.SignupPage, name='signup'),
    path('user/logi/',views.LoginPage, name='logi'),
    path('logout_user/', Logout_user, name='logout_user'),
    path('loggvt/', views.Login_govt, name='loggvt'),
    
     
]

