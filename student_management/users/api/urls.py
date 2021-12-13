from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from student_management.users.api.views import RegistrationApiView, account_logout

urlpatterns = [
	# Token
	path('login/', ObtainAuthToken.as_view(), name='login'),
	path('register/', RegistrationApiView.as_view(), name='register'),
	path('logout/', account_logout, name='logout'),

	# JWT
	path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]