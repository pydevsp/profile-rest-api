from django.urls import path
from  profiles_api import views


urlpatterns =[
    path('hello-view/',views.HelloApiView.as_view()),     
     #### as_view ===>standard function that we call to convert api view class to rendered
]