from django.urls import path, include
from . import views


app_name = 'decode_authe'

urlpatterns = [
    path('signup/',views.SignUpUser.as_view(), name='signup'),
    # path('entering/',views.EnterUser.as_view(), name='entering')
]