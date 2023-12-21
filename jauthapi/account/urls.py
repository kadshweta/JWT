from account.views import UserRegistrationView
from django.urls import path,include

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    # path('api/user/',include('account.urls'))
]

# api/user/register/