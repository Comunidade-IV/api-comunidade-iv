from django.urls import path
from .views import RegisterView, CustomAuthToken, RoleCreateView, RoleListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('roles/', RoleCreateView.as_view(), name='role_create'),
    path('roles/list/', RoleListView.as_view(), name='role_list'),
]