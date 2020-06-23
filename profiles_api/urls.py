from django.urls import path , include

from rest_framework.routers import DefaultRouter
from  profiles_api import views



router = DefaultRouter()
router.register('hello-viewwset',views.HelloViewSet,base_name = 'hello-viewwset')

urlpatterns =[
    path('hello-view/', views.HelloApiiView.as_view()),  
    #### as_view ===>standard function that we call to convert api view class to rendered   
    path('', include(router.urls)),
]