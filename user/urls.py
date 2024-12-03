from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, login_required, LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('signup/', views.registation, name='signup'),
    path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    path('', views.home, name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('delete_user/<int:user_id>/',views.delete_user, name='delete_user'),

]
