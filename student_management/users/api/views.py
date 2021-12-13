from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer, RegistrationSerializer

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class RegistrationApiView(APIView):

    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registration Successful'
            data['username'] = account.username
            data['email'] = account.email

            # # Token
            # token = Token.objects.get_or_create(user=account)
            # data['token'] = token[0].key

            # JWT
            refresh = RefreshToken.for_user(account)

            data['token'] = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
        else:
            data = serializer.errors
        
        return Response(data)


@api_view(['POST'])
def account_logout(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({'response': 'Logout Successful'}, status=status.HTTP_200_OK)
