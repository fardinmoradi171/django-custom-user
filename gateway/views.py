import string
import jwt
import random
from django.conf import settings
from datetime import datetime, timedelta 
from .models import Jwt
from user.models import CustomUser 
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .serializers import RegisterSerializer, RefreshSerializer,LoginSerializer
from .authentication import Authentication 
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def get_random(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def get_access_token(payload):
    return jwt.encode(
        {"exp": datetime.now() + timedelta(minutes=5), **payload},
        settings.SECRET_KEY,
        algorithm = "HS256"
                      )   
def get_refresh_token():
    return jwt.encode(
        {"exp": datetime.now() + timedelta(days=365), "data":get_random(10)},
        settings.SECRET_KEY,
        algorithm = "HS256"
                      )
class LoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['email'],
            password= serializer.validated_data['password'])
        if not user:
            return Response({"error":'invalid email or password'}, status="400")
        # remove the  existeed token:
        Jwt.objects.filter(user_id=user.id).delete()
        access = get_access_token({"user": user.id})
        refresh = get_refresh_token()
        Jwt.objects.create(
            user_id = user.id, access=access.decode(), refresh=refresh.decode()
        )
        return Response({"access":access,"refresh":refresh})
        
class RegisterView(APIView):
    serializer_class = RegisterSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        CustomUser.objects._create_user(**serializer.validated_data)
        return Response({"success":"user created."})
    

class RefreshView(APIView):
    serializer_class = RefreshSerializer
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        try:
            active_jwt = Jwt.objects.get(refresh = serializer.validated_data["refresh"])
        except Jwt.DoesNotExist:
            return Response({"error":"refresh token not exist"}, status="400")
        if not Authentication.verify_token(serializer.validated_data["refresh"]):
            return Response({"error":"toke is invalid or expired"})
            # redirect("login view")
        access = get_access_token({"user_id":active_jwt.user.id})
        refresh = get_refresh_token()
        # and here we can make the access and refresh decode() or not decode()
        active_jwt.access = access.decode()
        active_jwt.refresh = refresh.decode()
        active_jwt.save()
        return Response({"access": access, "refresh":refresh})
    

class GSI(APIView):
    authentication_classes = [Authentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        print(request.user)
        return Response({"date":"this is secured date"})
            