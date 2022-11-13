from django.urls import path,include
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('jobfunc/<str:pk>',views.jobfunc,name='jobs'),
    path('reviews',views.reviews,name='reviews'),
    path('contact',views.contact,name='contact'),
    path('jobsfilterdata',views.jobsfilterdata,name='jobsfilterdata'),
]