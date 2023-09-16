from django.urls import path
from .views import RegisterPage, LoginView, LogoutView, HomeView

urlpatterns = [
    path('signup/', RegisterPage.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
]
