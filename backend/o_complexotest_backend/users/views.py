from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (AllowAny, IsAuthenticated,)
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,

    HTTP_401_UNAUTHORIZED,
)

from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .models import UserModel
from .serializers import UserSerializer


class RegistrationAPIView(APIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
        }

        refresh_token = RefreshToken.for_user(user)
        refresh_token.payload.update(user_data)

        access_token = AccessToken.for_user(user)
        access_token.payload.update(user_data)

        if user.is_authenticated:
            return Response({
                'me': user.data_for_me,
                'refresh': str(refresh_token),
                'access': str(access_token),
            }, status=HTTP_201_CREATED)

        return Response(
            {'error': 'Not authenticated!'},
            status=HTTP_401_UNAUTHORIZED,
        )


class MeAPIView(APIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = self.serializer_class(request.user)

        return Response(
            serializer.data,
            status=HTTP_200_OK,
        )
