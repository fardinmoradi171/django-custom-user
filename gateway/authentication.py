from datetime import datetime
from django.conf import settings
import jwt


class Authentication():
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