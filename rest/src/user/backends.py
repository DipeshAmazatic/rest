from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import get_user_model
User = get_user_model()
class EmailOrPhone():
    def authenticate(self,request, username=None, password=None,**kwargs):
        try:
            # Check if the user exists in CustomUser database
            user = User.objects.get(Q(email=username)|Q(phone_no=username))
            if check_password(password, user.password):
                return user
        except User.DoesNotExist:
            pass
        return None

    # Required for the backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        return user if user.is_active else None

        