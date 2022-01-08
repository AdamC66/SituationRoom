from rest_framework import generics, permissions
from rest_framework.response import Response
from apps.situationroom_user.models import SituationRoomUser
from apps.situationroom_user.actions import create_user

from apps.situationroom_user.rest.serializers import UserSerializer, UserDetailSerializer, CreateUserSerializer
from django.contrib.auth import login
from rest_framework import permissions
from knox.models import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView



class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

class SituationRoomUserViewSet(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = SituationRoomUser.objects.all()
    
    def get(self, request, *args, **kwargs):
        user=request.user
        serializer = UserDetailSerializer(instance=user)
        return Response(serializer.data)

class RegistrationView(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = create_user(
            username=data.get("username"),
            password=data.get("password"),
            confirm_password=data.get("confirm_password"),
            email=data.get("email"),
        )
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })