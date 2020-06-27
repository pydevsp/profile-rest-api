from django.urls import path , include

from rest_framework.routers import DefaultRouter
from  profiles_api import views



router = DefaultRouter()
router.register('hello-viewwset',views.HelloViewSet,base_name = 'hello-viewwset') #### SERVER ===> :8000/api
router.register('profile',views.UserProfileViewSet)   #### server ===> :8000/api/profile
router.register('feed' , views.UserProfileFeedViewSet)

urlpatterns =[
    path('hello-view/', views.HelloApiiView.as_view()),  ######## server ===> :8000/api/hello-view
    #### as_view ===>standard function that we call for convert api view class to rendered   
    path('login/' , views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]