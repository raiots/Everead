from django.urls import path, include

# 引入views.py
from . import views


app_name = 'users'


urlpatterns = [
    # path函数将url映射到视图
    path('profile/', views.UserProfileView.as_view(), name='profile'),
]