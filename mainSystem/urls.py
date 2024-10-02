from django.urls import path
from .views import all_data_view,login_view,logout_view,kafedralar_jadvali

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin/',kafedralar_jadvali, name='admin'),


    path('', all_data_view, name='home'),
]
