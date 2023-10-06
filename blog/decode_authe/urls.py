from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views


app_name = 'decode_authe'

urlpatterns = [
    path('signup/',views.SignUpUser.as_view(), name='signup'),
    path('signin/',views.SignInUser.as_view() ,name='signin'),
    path('signout/',views.signout_user , name='signout'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/user/', views.UserViewSet.as_view({'get': 'retrieve', 'post': 'create'})),

]