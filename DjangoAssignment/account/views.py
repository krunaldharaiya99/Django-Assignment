# Rest Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Import models
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken

# Import serializers
from account.serializers import UserSerializer, UserLoginSerializer, UserProfileSerializer

# Other Imports
from django.contrib.auth import authenticate

# Generate Token Manually
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),

    }

class UserLoginAPIView(APIView):
    '''
    User Login API View
    '''
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_token_for_user(user)
                return Response({'token':token, 'message': 'Login Successfull..!'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {
                    'non_field_errors' : ['Email or Password is not valid..!']
                }}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

user_login_view = UserLoginAPIView.as_view()


class UserRegistrationAPIView(APIView):
    '''
    User Registration API View
    '''
    renderer_class = [UserRenderer]
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_token_for_user(user)
            return Response({'token': token, 'message':'Resgistration successfully '}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

user_registration_view = UserRegistrationAPIView.as_view()


class UserProfileAPIView(APIView):
    '''
    User Profile API View
    '''
    renderer_class = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

user_profile_view = UserProfileAPIView.as_view()