from datetime import datetime
from django.conf import settings
import jwt
from rest_framework.authentication import BaseAuthentication
from user.models import CustomUser


class Authentication(BaseAuthentication):
    def authenticate(self,request):
        data = self.validate_request(request.headers)
        print(data)
        if not data:
            return None, None
        return self.get_user(data["user"]), None
    
    def get_user(self,user):
        try:
            user = CustomUser.objects.get(id=user)
            return user
        except Exception:
            return None
    
    def validate_request(self,headers):
        authorization = headers.get("Authorization",None)
        if not authorization:
            # raise Exception("you need to provide authoraization token")
            return None
            # return Response({"error":"you need authorization.."})
        token = headers["Authorization"][7:]
        decoded_data = Authentication.verify_token(token)
        # print("verify_token")
        if not decoded_data:
            # raise Exception("token not valid or expired")
            return None
        return decoded_data
    
    @staticmethod
    def verify_token(token):
        try:
            decoded_data = jwt.decode(token,settings.SECRET_KEY, algorithm="HS256")
        except Exception:
            return None
        exp = decoded_data["exp"]
        if datetime.now().timestamp() > exp:
            return None
        return decoded_data