from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer, RegisterUserSerializer


class RegisterUser(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterUserSerializer
    def post(self,request,format="json"):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            try:
                newUser = serializer.save()
                if newUser:
                    response = serializer.data
                    return Response(response, status=status.HTTP_201_CREATED)
                
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors or None, status=status.HTTP_400_BAD_REQUEST)
    

class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlacklistTokenAdding(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format='json'):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)