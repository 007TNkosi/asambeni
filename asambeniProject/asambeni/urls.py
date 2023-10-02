from django.urls import path
from asambeni import views
from .views import DriverSignUpView, LearnerSignUpView, admin_dash, learner_dash, driver_dash

urlpatterns = [
    ## -_-_ Pages
    path('', views.index, name ='index'),
    path('about-us/', views.aboutUs, name='about'),

    ## -_-_ Users Urls
    path('signup/learner/', views.LearnerSignUpView, name='learner_signup'),
    path('signup/driver/', views.DriverSignUpView.as_view(), name='driver_signup'),
    path('user_logout/', views.user_logout, name ='logout'),

    ## -_-_ Logged In Views
    path('admin_dash/', views.admin_dash, name ='admin'),
    path('learner_dash/', views.learner_dash, name ='learner'),
    path('driver_dash/', views.driver_dash, name ='driver'),
]