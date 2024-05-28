from django.urls import path
from .views import RegisterView, LoginView
from .views import AssociateKeazyView, OpenDeviceView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('associate-keazy/', AssociateKeazyView.as_view(), name='associate-keazy'),
    path('open-device/', OpenDeviceView.as_view(), name='open-device'),
]
