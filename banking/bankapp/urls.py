from . import views
from django.urls import path

app_name='bankapp'
urlpatterns= [
    path('',views.home,name='home'),
    path('register/',views.registration,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('content/',views.content,name='content'),


    path('add/',views.person_create_view,name='person_add'),

    path('ajax/load_branches/',views.load_branches,name='load_branches'),
]