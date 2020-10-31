from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'), # get and post re for insert operation
    path('<int:id>/', views.employee_form, name='employee_update'), # get and post re for update operation


    
    path('delete/<int:id>/',views.employee_delete, name='employee_delete'),
    path('list/',views.employee_list, name='employee_list'), # get req and display all records 

    path('home', views.home, name='home'),


    path('login1', views.login1, name = 'login1'),
    path('signup', views.signup, name = 'signup')




   	# path('delete/<int:id>/', views.employee_delete, name='employee_delete')
]
