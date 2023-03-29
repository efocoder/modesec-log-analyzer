from django.urls import path

from users.views import RegistrationView, LoginView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login')
]
