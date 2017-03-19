from rest_framework import generics, permissions, response
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import LoginSerializer, UserSerializer


class AuthView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        s = self.get_serializer(data=request.data)
        if s.is_valid():
            username = s.validated_data['username']
            password = s.validated_data['password']
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    token = Token.objects.get_or_create(user=user)[0]
                    return response.Response({
                        'status': 'success',
                        'token': token.key,
                        'user': UserSerializer(instance=user).data
                    })
            except User.DoesNotExist:
                pass
        return response.Response({
            'status': 'invalid',
        })
