from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='Home'),
    path('make_req/',views.make_request, name='make_request'),

]